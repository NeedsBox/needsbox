from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

from .models import Account, PublicContacts


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
class UpdateForm(forms.Form):
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

    class Meta:
        model = Account
        fields = (
            'username',
            'email',
            'name',
        )

# creating a form 
class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = Account 
        fields = (
            'name',
            'profile_image',
            'biography',
            'small_biography',
            'contact',
            'account_type',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'account_type': forms.Select(
                attrs={
                    'class': 'form-control',
                },

            ),
            'small_biography': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'biography': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'contact': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                },
            ),
        }

class PublicContactsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(PublicContactsForm, self).__init__(*args, **kwargs)
    class Meta:
        model = PublicContacts
        fields = [
            
            'email',
            'phone',
            'address',
        ]
