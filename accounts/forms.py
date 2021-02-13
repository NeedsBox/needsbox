from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Account

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