# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models


class Advertisement(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=512)
    category = models.ForeignKey('Category', models.DO_NOTHING)
    location = models.ForeignKey('UserLocation', models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    ad_type = models.ForeignKey('AdvertisementType', models.DO_NOTHING, db_column='ad_type')

    class Meta:
        db_table = 'ad'


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ad_type'


class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'


class Contact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    contact = models.CharField(max_length=512)
    contact_type = models.ForeignKey('ContactType', models.DO_NOTHING, db_column='contact_type', blank=True, null=True)

    class Meta:
        db_table = 'contact'


class ContactType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'contact_type'


class Review(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    description = models.CharField(max_length=512)
    ranking = models.FloatField()
    user = models.ForeignKey(User, models.DO_NOTHING)
    ad = models.ForeignKey(Advertisement, models.DO_NOTHING)

    class Meta:
        db_table = 'review'


class UserLocation(models.Model):
    id = models.IntegerField(unique=True)
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    loc = models.TextField()  # This field type is a guess.
    description = models.CharField(max_length=512)

    class Meta:
        db_table = 'user_location'
        unique_together = (('user', 'id'),)


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    default_ad_type = models.ForeignKey(AdvertisementType, models.DO_NOTHING, db_column='default_ad_type', blank=True,
                                        null=True)

    class Meta:
        db_table = 'user_profile'
