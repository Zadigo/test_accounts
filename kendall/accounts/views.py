import datetime
import re

from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import (PasswordChangeForm, PasswordResetForm,
                                       SetPasswordForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import add_message
from django.core.mail import BadHeaderError, send_mail
from django.http.response import HttpResponseForbidden
from django.shortcuts import (Http404, HttpResponse, get_object_or_404,
                              redirect, render, reverse)
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views.generic import View

from accounts.forms import (AddressProfileForm, BaseProfileForm, UserLoginForm,
                            UserSignupForm)
from accounts.models import AccountsToken, MyUser, MyUserProfile






# #####################
#  REGISTRATION VIEWS
# #####################


class SignupView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'consent': True,
            'form': UserSignupForm,
            'form_button_registration': _("S'enregistrer")
        }
        return render(request, 'registration/signup.html', context)

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
        return render(request, 'registration/login.html', context)

    def post(self, request, **kwargs):
        email       = request.POST['username']
        password    = request.POST['password']
        user        = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next') or 'home')

        else:
            add_message(request, messages.WARNING, message=_("Nous n'arrivons pas à vous connectez"))
            return redirect('home')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': PasswordChangeForm(request.user),
            'form_button_registration': _('Modifier')
        }
        return render(request, 'accounts/profile_password_reset.html', context)

    def post(self, request, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # IMPORTANT to allow the user to stay logged
            update_session_auth_hash(request, user)
        return redirect('/profile/')


class ForgotPasswordView(View):
    """This class helps the user reset his password 
    when he has difficulties authenticating
    """
    def get(self, request, *args, **kwargs):
        context = {
            'form': PasswordResetForm,
            'form_button_registration': _('Nouveau mot de passe')
        }

        return render(request, 'registration/forgot_password.html', context)

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
                return render(request, 'registration/forgot_password.html', context=context)

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
        return render(request, 'registration/forgot_password_confirm.html', context)

    def post(self, request, **kwargs):
        user_token = request.GET.get('user_token')
        user = get_object_or_404(MyUser, id=user_token)
        form = SetPasswordForm(user)
        if form.is_valid():
            form.save()
        login(request, user)
        return redirect('/profile/')


# #####################
#   PROFILE VIEWS
# #####################

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, id=request.user.id)
        profile = user.myuserprofile_set.get(myuser=request.user.id)

        context = {
            'base_profile_form': BaseProfileForm(
                initial = {
                    'nom': user.nom,
                    'prenom': user.prenom
                }
            ),
            'address_profile_form': AddressProfileForm(
                initial = {
                    'adresse': profile.adresse,
                    'ville': profile.ville,
                    'code_postal': profile.code_postal
                }
            )
        }

        return render(request, 'accounts/profile_profile.html', context)

    def post(self, request, **kwargs):
        # USING AJAX

        user_id = request.user
        user = MyUser.objects.get(id=user_id.id)
        user_profile = user.myuserprofile_set.get(myuser_id_id=user_id.id)

        form_id = request.POST.get('form_id')
        if form_id == 'base-profile-form':
            form = BaseProfileForm(request.POST, instance=user)

        if form_id == 'address-profile-form':
            form = AddressProfileForm(request.POST, instance=user_profile)

        if form.is_valid():
            form.save()

        return redirect('/profile/')


class ProfileDataView(LoginRequiredMixin, View):
    """Help the user manage his data
    """
    def get(self, request, *args, **kwargs):
        current_user = self.request.user

        # Query the social_auth database and
        # get a set of connected accounts
        user = self.request.user.social_auth.get(uid=current_user.email)
        if user:
            context = {
                'provider': user.provider
            }

        return render(request, 'accounts/profile_data.html', context)


class ProfileDeleteView(LoginRequiredMixin, View):
    """Help the user delete his account
    """
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, id=request.user.id)
        user.delete()
        return redirect('/')

class PaymentMethodsView(LoginRequiredMixin, View):
    """Allows the customer to update his/her payment method"""
    
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/payment_methods.html', {})

    def post(self, request, *kwargs):
        try:
            import stripe
        except ImportError:
            raise Http404('An error has occured')
        else:
            # We can update the customer's cards here
            # using the stripe api
            params = {
                'source': 'source'
            }
            stripe.Customer.update(**params)
        finally:
            response = {
                'status': ''
            }
        return JsonResponse(response)

# class PersonalisationView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         context = {
#             'user_profile':self.get_user_profile,
#             'form': PersonalizationProfileForm
#         }
#         return render(request, 'accounts/profile_personalisation.html', context)

#     def post(self, request, **kwargs):
#         user_profile = self.get_user_profile
#         redirect('personalisation')

#     @property
#     def get_user_profile(self):
#         return MyUserProfile.objects.get(myuser_id_id=self.request.user.id)
