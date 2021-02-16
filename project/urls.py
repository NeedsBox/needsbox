from django.urls import path

from . import views

app_name = 'needsbox'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('create/', views.ServiceCreate.as_view(), name="service_form"),
    path('create_ad/', views.AdvertisementCreate.as_view(), name="advertisement_form"),
    path('<int:pk>/update_ad/', views.AdvertisementUpdate.as_view(), name="advertisement_update_form"),
    path('<int:pk>/delete_ad/', views.AdvertisementDelete.as_view(), name="advertisement_confirm_delete"),
    path('<int:pk>/update/', views.ServiceUpdate.as_view(), name="service_update"),
    path('<int:pk>/delete/', views.ServiceDelete.as_view(), name="service_delete"),
    path('<int:pk>/service/', views.ServiceDetail.as_view(), name="service_detail"),

]
