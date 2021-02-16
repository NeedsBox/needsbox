from django.urls import path

from . import views

app_name = 'needsbox'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('ad/create/', views.AdvertisementCreate.as_view(), name="advertisement_form"),
    path('ad/<int:pk>/update/', views.AdvertisementUpdate.as_view(), name="advertisement_update_form"),
    path('ad/<int:pk>/delete/', views.AdvertisementDelete.as_view(), name="advertisement_confirm_delete"),
    path('service/create/', views.ServiceCreate.as_view(), name="service_form"),
    path('service/<int:pk>/', views.ServiceDetail.as_view(), name="service_detail"),
    path('service/<int:pk>/update/', views.ServiceUpdate.as_view(), name="service_update"),
    path('service/<int:pk>/delete/', views.ServiceDelete.as_view(), name="service_delete"),

]
