from django.urls import path, include

from .views import (
    PostCreateView,
    PostsListView,
    PostDetail,
    PostUpdate
)

app_name = 'post'
urlpatterns = [
    path('', PostsListView.as_view(), name='home-view'),
    path('<int:id>/', PostDetail.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:id>/update/', PostUpdate.as_view(), name='post-update'),
    
]