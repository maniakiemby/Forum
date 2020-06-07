from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    FormView,
)

from .forms import PostForm, CreateUserForm
from .models import Post, Comment

# LoginRequiredMixin służy do autoryzacji
class PostCreateView(LoginRequiredMixin, CreateView):
    pass


class PostsListView(ListView):
    template_name = 'post/posts_list.html'
    queryset = Post.objects.all()


class PostDetail(DetailView):
    template_name = 'post/post_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)


class CreateUserView(FormView):
    template_name = 'registration/registration.html'
    form_class = CreateUserForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(CreateUserView, self).form_valid(form)

