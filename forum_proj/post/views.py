from django.shortcuts import render
from django.views import View
from django.views.generic import (
    CreateView
)

from .forms import PostForm
from .models import Post, Comment


class PostCreateView(CreateView):
    pass