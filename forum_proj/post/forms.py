from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Post, Comment
from user_panel.models import Users


class PostForm(forms.ModelForm):
    #author = forms.ModelChoiceField(queryset=Users.objects.all())
    title = forms.CharField(max_length=200)
    content = forms.CharField(
        widget=forms.TextInput(),
        strip=False,
        max_length=10000
    )


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
          
    class Meta:
        model = Post
        fields = [
            #'author',
            'title',
            'content'
