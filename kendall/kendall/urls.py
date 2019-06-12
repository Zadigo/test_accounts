from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='hero/hero.html'), name='home'),
    path('admin/', admin.site.urls)
]
