from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('user_panel.Users', on_delete=models.CASCADE, max_length=50)
    title = models.CharField(max_length=200)
    content = models.CharField(editable=True, max_length=10000)
    date_modified = models.DateTimeField(auto_now=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post-detail', kwargs={'id': self.id})


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('user_panel.Users', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date_create = models.DateTimeField(auto_now_add=True)

