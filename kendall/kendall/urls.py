from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from kendall.views import Home

urlpatterns = [
    path('api/v1/', include('api.urls')),

    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    
    path('', Home.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
