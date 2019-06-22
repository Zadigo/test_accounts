from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from accounts.rest_views import UserProfileSerializer, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, base_name='users')

urlpatterns = [
    url(r'^api/v1/auth/obtain-token/$', obtain_jwt_token, name='obtain_token'),
    url(r'^api/v1/auth/refresh-token/', refresh_jwt_token, name='refresh_token'),

    path('api/v1/', include(router.urls)),

    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    
    path('', TemplateView.as_view(template_name='hero/hero.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
