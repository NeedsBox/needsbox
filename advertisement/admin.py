from django.contrib import admin

# Register your models here.
from advertisement.models import *


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(AdvertisementRating)
admin.site.register(AdvertisementComment)
