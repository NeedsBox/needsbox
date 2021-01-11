from django.urls import path, include
from . import views

urlpatterns = [
    path('advertisements', views.adList, name="advertisements"),
    path('users', views.userList, name="users"),
]