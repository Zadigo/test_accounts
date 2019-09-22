from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from accounts import views as registration_views
import views_profile

urlpatterns = [
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^profile/payment-methods/$', views_profile.PaymentMethodsView.as_view(), name='payment_methods'),
    # url(r'^profile/personalisation/$', views.PersonalisationView.as_view(), name='personalisation'),
    url(r'^profile/delete/$', views_profile.ProfileDeleteView.as_view(), name='delete_account'),
    url(r'^profile/data/$', views_profile.ProfileDataView.as_view(), name='profile_data'),
    url(r'^profile/change-password/$', views_profile.ChangePasswordView.as_view(), name='change_password'),
    
    url(r'^forgot-password/confirm/(?P<uidb64>[A-Z]+)/(?P<token>\d+\w?\-[a-z0-9]+)', 
            registration_views.UnauthenticatedChangePasswordView.as_view(), name='password_reset_confirm'),
    url(r'^forgot-password/$', registration_views.ForgotPasswordView.as_view(), name='forgot_password'),
    url(r'^login/$', registration_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', registration_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', registration_views.SignupView.as_view(), name='signup'),

    url(r'^profile/$', views_profile.ProfileView.as_view(), name='profile'),
]
