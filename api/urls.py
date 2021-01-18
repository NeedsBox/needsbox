from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api import views
from api.views import AdListView, ServiceViewSet, UserViewSet, CategoryViewSet, AdViewSet, ServiceListView

router = routers.DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/sessions', obtain_auth_token),
    path('users/sessions/<str:token>', views.verify_token),
    path('search/ads/', AdListView.as_view()),
    path('search/services/', ServiceListView.as_view()),
]
