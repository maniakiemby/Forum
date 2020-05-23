from django.db import models


class Post(models.Model):
    author = models.ForeignKey('authenticate.Users', on_delete=models.CASCADE, max_length=50)
    title = models.CharField(max_length=200)
    content = models.CharField(editable=True, max_length=10000)
    date_modified = models.DateTimeField(auto_now=True)
    date_create = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)

    def _str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('Post', on_delete=models.CASCADE, max_length=50)
    content = models.CharField(max_length=500)
    date_create = models.DateTimeField(auto_now_add=True)

