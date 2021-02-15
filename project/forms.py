from django import forms
from mapwidgets.widgets import GooglePointFieldWidget

from project.models import Service


class AddServiceForm(forms.ModelForm):
    image = forms.ImageField(),

    class Meta:
        model = Service
        fields = [
            'category',
            'title',
            'description',
            'price',
            'location',
            'image',
        ]

        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'location': GooglePointFieldWidget,
        }


class UpdateServiceForm(forms.ModelForm):
    image = forms.ImageField(),

    class Meta:
        model = Service
        fields = [
            'category',
            'title',
            'description',
            'price',
            'location',
            'image',
        ]

        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'location': GooglePointFieldWidget,
        }
