from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from accounts import views



urlpatterns = [
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # url(r'^profile/personalisation/$', views.PersonalisationView.as_view(), name='personalisation'),
    url(r'^profile/delete/$', views.ProfileDeleteView.as_view(), name='delete_account'),
    url(r'^profile/data/$', views.ProfileDataView.as_view(), name='profile_data'),
    url(r'^profile/change-password/$', views.ChangePasswordView.as_view(), name='change_password'),
    url(r'^forgot-password/confirm/(?P<uidb64>[A-Z]+)/(?P<token>539\-[a-z0-9]+)', 
            views.UnauthenticatedChangePasswordView.as_view(), name='password_reset_confirm'),
    url(r'^forgot-password/$', views.ForgotPasswordView.as_view(), name='forgot_password'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    # url(r'^$', views.accounts_redirection, name='accounts_redirection'),
]