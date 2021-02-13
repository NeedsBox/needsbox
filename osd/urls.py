from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from rest_framework import routers

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sign-in/', auth_views.LoginView.as_view(template_name='sign-in.html'), name='sign-in'),
    path('sign-up/', auth_views.LogoutView.as_view(template_name='sign-up.html'), name='sign-up'),
]

# url para media, apenas manter em desenvolvimento, não pode ser assim em produção
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
