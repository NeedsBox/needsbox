from django.conf import settings
from django.contrib import admin
from django.db import models
from django.conf import settings


class Advertisement(models.Model):
    title = models.CharField(max_length=65535)
    description = models.CharField(max_length=65535)
    price = models.DecimalField(max_digits=1000, decimal_places=1000)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    date_publication = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'advertisement'


class AdvertisementComment(models.Model):
    id = models.IntegerField(primary_key=True)
    advertisement = models.ForeignKey(Advertisement, models.DO_NOTHING)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    content = models.CharField(max_length=65535)

    class Meta:
        db_table = 'advertisement_comment'


class AdvertisementRating(models.Model):
    advertisement = models.ForeignKey(Advertisement, models.DO_NOTHING)
    star_rating = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'advertisement_rating'


class AdvertisementRatingInline(admin.TabularInline):
    model = AdvertisementRating


class AdvertisementAdmin(admin.ModelAdmin):
    inlines = (AdvertisementRatingInline,)