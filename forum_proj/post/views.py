from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from .forms import PostForm, CommentForm
from .models import Post, Comment


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "../user/accounts/login/"
    template_name = "post/post_create.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostsListView(ListView):
    template_name = "post/posts_list.html"
    queryset = Post.objects.all()
    paginate_by = 20


class PostDetailView(View):
    template_name = "post/post_detail.html"
    allow_empty = True

    def get(self, request, post_id=None, *args, **kwargs):
        context = {}
        if post_id is not None:
            queryset = Comment.objects.filter(post_id=post_id)
            obj = get_object_or_404(Post, id=post_id)
            form = CommentForm()
            if queryset.exists():
                comments = get_list_or_404(queryset)
                context['object'] = obj
                context['comments'] = comments
                context['form'] = form
            else:
                context['object'] = obj
                context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, post_id=None, *args, **kwargs):
        form = CommentForm(request.POST)
        form.instance.author = self.request.user
        form.instance.post_id = post_id
        if form.is_valid():
            form.save()
            form = CommentForm()
            return redirect('.')
        return render(request, self.template_name)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "../user/accounts/login/"
    template_name = "post/post_update.html"
    form_class = PostForm
    success_url = "../"

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(Post, id=post_id)

    def form_valid(self, form):
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    login_url = "../user/accounts/login/"
    template_name = "post/post_delete_confirmation.html"
    success_url = "../../"

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "../user/accounts/login/"
    template_name = "post/comment_edit.html"
    form_class = CommentForm
    success_url = "../../"

    def get_object(self):
        comment_id = self.kwargs.get("comment_id")
        return get_object_or_404(Comment, id=comment_id)

    def form_valid(self, form):
        return super().form_valid(form)


class CommentDelete(LoginRequiredMixin, DeleteView):
    login_url = "../user/accounts/login/"
    template_name = "post/comment_delete_confirmation.html"
    success_url = "../../"

    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        return get_object_or_404(Comment, id=comment_id)

