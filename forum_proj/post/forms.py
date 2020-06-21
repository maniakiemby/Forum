from django.contrib.auth.models import User
from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='Tu wpisz tytuł',
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'cols': 75,
                'rows': 5
            }
        ),
    )
    content = forms.CharField(
        label='Tutaj opisz swój pomysł',
        widget=forms.Textarea(
            attrs={
                'cols': 75,
                'rows': 50
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
                'placeholder': "Dodaj swój komentarz..",
                'class': "new-class-name two",
            },
        )
    )

    class Meta:
        model = Comment
        fields = [
            'content',
        ]
