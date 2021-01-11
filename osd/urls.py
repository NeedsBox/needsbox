from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# url para media, apenas manter em desenvolvimento, não pode ser assim em produção
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
