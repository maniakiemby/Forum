from django.urls import path, include

from .views import (
    PostCreateView,
    PostsListView,
    PostDetailView,
    PostUpdateView,
    PostDelete,
    CommentUpdateView,
    CommentDelete,

)

app_name = 'post'
urlpatterns = [
    path('', PostsListView.as_view(), name='home-view'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:post_id>/delete/', PostDelete.as_view(), name='post-delete'),
    path('<int:post_id>/<int:comment_id>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('<int:post_id>/<int:comment_id>/delete/', CommentDelete.as_view(), name='comment-delete'),
]