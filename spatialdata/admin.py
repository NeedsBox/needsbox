from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Limits

@admin.register(Limits)

# Class para poder ter um mapa para inserir dados espaciais no /admin
class LimitsAdmin(OSMGeoAdmin):
    list_display = (
        'id',
        'concelho',
        'distrito_title',
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(LimitsAdmin, self).get_form(request, obj, **kwargs)
        return form