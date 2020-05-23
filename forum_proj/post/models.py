from django.db import models


class Post(models.Model):
    author = models.ForeignKey('authenticate.Users', on_delete=models.SET_NULL, max_length=50, null=True)
    content = models.CharField(editable=True, max_length=5000)
    is_active = models.BooleanField(default=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_create = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)


class Comment(models.Model):
    author = models.ForeignKey('authenticate.Users', on_delete=models.SET_NULL, max_length=50, null=True)
    content = models.CharField(editable=True, max_length=1000)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    little_comments = models.ForeignKey('LittleComment', on_delete=models.CASCADE, blank=True, null=True)
