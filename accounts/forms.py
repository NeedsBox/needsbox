from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Account


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }
    ), label='')
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control',
        }
    ), label='')
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Name',
            'class': 'form-control',
        }
    ), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }
    ), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
        }
    ), label='')

    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'name',
            'password1',
            'password2'
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }
    ), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }
    ), label='')

    class Meta:
        model = AuthenticationForm
        fields = (
            'username',
            'password',
        )
