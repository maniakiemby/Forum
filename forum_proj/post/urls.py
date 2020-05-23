from django.urls import path, include

from .views import PostCreateView

app_name = 'post'
urlpatterns = [
    path('', PostCreateView.as_view(), name='post-create')
]