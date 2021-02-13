from django.contrib import admin
from .models import Category, Advertisement, Review, Service
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.

admin.site.register(Category)
admin.site.register(Review)

@admin.register(Advertisement, Service)

# Class para poder ter um mapa para inserir dados espaciais no /admin
class AdvertisementAdmin(OSMGeoAdmin):
    list_display = (
        'id',
        'title',
        'description',
    )

class ServiceAdmin(OSMGeoAdmin):
    list_display = (
        'id',
        'title',
        'description',
    )