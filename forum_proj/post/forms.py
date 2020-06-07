from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
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
        ]
