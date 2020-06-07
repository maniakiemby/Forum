from django.urls import path, include

from .views import (
    PostCreateView,
    PostsListView,
    PostDetail,
    # CreateUser,
    CreateUserView,
)

app_name = 'post'
urlpatterns = [
    path('', PostsListView.as_view(), name='home-view'),
    path('<int:id>/', PostDetail.as_view(), name='post-detail'),

    path('registration/', CreateUserView.as_view(), name='create-user')
    #path('create/', PostCreateView.as_view(), name='post-create')

    path('create/', PostCreateView.as_view(), name='post-create'),
  
]