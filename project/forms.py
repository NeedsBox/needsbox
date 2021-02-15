from django import forms
from mapwidgets.widgets import GooglePointFieldWidget

from project.models import Service


class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

        widgets = {
            'location': GooglePointFieldWidget,
        }
