from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    FormView,
    
)

from .forms import PostForm
from .models import Post, Comment


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "../user/accounts/login/"
    template_name = 'post/post_create.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostsListView(ListView):
    template_name = 'post/posts_list.html'
    queryset = Post.objects.all()


class PostDetail(DetailView):
    template_name = 'post/post_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)


class PostUpdate(LoginRequiredMixin, UpdateView):
    login_url = "../user/accounts/login/"
    template_name = 'post/post_update.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def form_valid(self, form):
        #print(form.cleaned_data)
        return super().form_valid(form)

