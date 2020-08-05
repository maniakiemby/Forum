from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from django.contrib.auth.models import User
from django import forms


# email - unique

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label = '',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nazwa użytkownika',
                'cols': 30,
                'rows': 1,
                'class': 'label'
            },
        ),
    )
    email = forms.EmailField(
        label = '',
        widget = forms.EmailInput(
            attrs={
                'placeholder': 'E-mail',
                'class': 'label'
            },
        ),
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Hasło',
                'class': 'label'
            }
        )
    )
    password2 = forms.CharField(
        label = '',
        widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Potwierdzenie hasła',
                'class': 'label'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(
        label = 'Imię',
        widget = forms.TextInput(
            attrs={
                'cols': 30,
                'rows': 1,
                'class': 'input-label'
            }
        )
    )
    last_name = forms.CharField(
        label = 'Nazwisko',
        widget = forms.TextInput(
            attrs={
                'cols': 30,
                'rows': 1,
                'class': 'input-label'
            }
        )
    )
    email = forms.CharField(
        label = 'E-mail',
        widget = forms.TextInput(
            attrs={
                'cols': 30,
                'rows': 1,
                'class': 'input-label'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]
        exclude = [
            'username',
            'password',
            'is_staff',
            'is_active'
        ]
