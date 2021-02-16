from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

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


class ResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control',
        }
    ), label='')


class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Nova Palavra-passe',
            'class': 'form-control',
            'type': 'password',
        }
    ), label='')

    new_password2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Confirmação da Palavra-passe',
            'class': 'form-control',
            'type': 'password',
        }
    ), label='')
