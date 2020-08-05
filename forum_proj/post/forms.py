from django.contrib.auth.models import User
from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'cols': 75,
                'rows': 5,
                'placeholder': 'Tu wpisz tytuł'
            }
        ),
    )
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'cols': 75,
                'rows': 30,
                'placeholder': 'Tutaj opisz swój pomysł'
            }
        ),
        strip=False,
        max_length=10000,
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'cols': 75,
                'rows': 1,
                'placeholder': "Dodaj swój komentarz..",
                'class': "add-comment-widget"
            },
        )
    )

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
