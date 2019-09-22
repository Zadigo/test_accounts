import datetime
import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import (PasswordChangeForm, PasswordResetForm,
                                       SetPasswordForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import BadHeaderError, send_mail
from django.http.response import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views.generic import View

from accounts.models import AccountsToken, MyUser, MyUserProfile
from accounts.forms import UserLoginForm, UserSignupForm


class SignupView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'consent': True,
            'form': UserSignupForm,
            'form_button_registration': _("S'enregistrer")
        }
        return render(request, 'registration/pages/signup.html', context)

    def post(self, request, **kwargs):
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        password = request.POST['password']

        user_exists = MyUser.objects.filter(email__iexact=email).exists()
        if user_exists:
            return redirect(reverse('profile'))
            
        else:
            user = MyUser.objects.create_user(
                        email, nom=nom, prenom=prenom, password=password)

            if user:
                login(request, authenticate(request, email=email, password=password))
                return redirect(request.GET.get('next') or reverse('profile'))
   

class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': UserLoginForm,
            'form_button_registration': _('Se connecter')
        }
        return render(request, 'registration/pages/login.html', context)

    def post(self, request, **kwargs):
        email       = request.POST['username']
        password    = request.POST['password']
        user        = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next') or 'profile')

        else:
            # add_message(request, messages.WARNING, message=_("Nous n'arrivons pas à vous connectez"))
            return redirect('login')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class ForgotPasswordView(View):
    """This class helps the user reset his password 
    by sendind himself an email with a link in order to
    reset his password
    """
    def get(self, request, *args, **kwargs):
        context = {
            'form': PasswordResetForm,
            'form_button_registration': _('Nouveau mot de passe')
        }

        return render(request, 'registration/pages/forgot_password.html', context)

    def post(self, request, **kwargs):
        # Get the POST request
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            user = MyUser.objects.filter(email__iexact=email)
            if user.exists():
                # NOTE: Change to append a token to the url
                # which will help iD the user in the confirm view
                form.save(from_email='pendenquejohn@gmail.com', request=request)

            else:
                form.errors['email'] = _("Nous n'avons pas pu vous trouvez votre addresse mail")
                context = {
                    'form': PasswordResetForm,
                    'form_button_registration': _('Nouveau mot de passe')
                }
                return render(request, 'registration/pages/forgot_password.html', context=context)

        return redirect('login')


class UnauthenticatedChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        user_token = request.GET.get('user_token')
        if not user_token:
            return HttpResponseForbidden(reason='Missing argument')
        
        context = {
            'form': SetPasswordForm(MyUser.objects.get(id=1)),
            'form_button_registration': _('Modifier')
        }
        return render(request, 'registration/pages/forgot_password_confirm.html', context)

    def post(self, request, **kwargs):
        user_token = request.GET.get('user_token')
        user = get_object_or_404(MyUser, id=user_token)
        form = SetPasswordForm(user)
        if form.is_valid():
            form.save()
        login(request, user)
        return redirect('/profile/')
