from django.contrib import admin
from .models import Category, Advertisement, Review
# Register your models here.

admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(Review)