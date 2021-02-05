from django.conf.urls import url
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_extensions.routers import ExtendedDefaultRouter

from api import views
from api.views import AdListView, ServiceViewSet, UserViewSet, CategoryViewSet, AdViewSet, ServiceListView, \
    ReviewViewSet

# Documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="NeedsBox API",
      default_version='v1',
      description="This is the documentation for the NeedsBox API!",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
# End of Documentation

router = ExtendedDefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'services', ServiceViewSet) \
    .register(r'reviews', ReviewViewSet, parents_query_lookups=['service_id'], basename="reviews")
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/sessions', obtain_auth_token),
    path('users/sessions/<str:token>', views.verify_token),
    path('search/ads/', AdListView.as_view()),
    path('search/services/', ServiceListView.as_view()),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
