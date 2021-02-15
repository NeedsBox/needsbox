from mapwidgets.widgets import GooglePointFieldWidget

from project.models import Service


class AddForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'name',
            'location',
        )

        widgets = {
            'location': GooglePointFieldWidget,
        }
