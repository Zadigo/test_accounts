from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views.generic import View

from accounts.forms import AddressProfileForm, BaseProfileForm, NewPaymentMethodForm
from accounts.models import MyUser, MyUserProfile


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = MyUserProfile.profile.related_user(request.user)
        if not user:
            raise Http404()

        # user = get_object_or_404(MyUser, id=request.user.id)
        # profile = user.myuserprofile_set.get(myuser=user)

        context = {
            'base_profile_form': BaseProfileForm(
                initial = {
                    'nom': user.myuser.nom,
                    'prenom': user.myuser.prenom
                }
            ),
            'address_profile_form': AddressProfileForm(
                initial = {
                    'adresse': user.adresse,
                    'ville': user.ville,
                    'code_postal': user.code_postal
                }
            )
        }

        return render(request, 'accounts/pages/profile.html', context)

    def post(self, request, **kwargs):
        # AJAX

        user = MyUserProfile.profile.related_user(request.user)
        
        form_id = request.POST.get('form_id')
        if form_id == 'base-profile-form':
            form = BaseProfileForm(request.POST, instance=user.myuser)

        if form_id == 'address-profile-form':
            form = AddressProfileForm(request.POST, instance=user)

        if form:
            if form.is_valid():
                form.save()
                response = {'status': 'success'}
        else:
            response = {'status': 'error'}

        return JsonResponse(response)


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': PasswordChangeForm(request.user),
            'form_button_registration': _('Modifier')
        }
        return render(request, 'accounts/pages/password_reset.html', context)

    def post(self, request, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # IMPORTANT to allow the user to stay logged
            update_session_auth_hash(request, user)
        return redirect('/profile/')


class ProfileDataView(LoginRequiredMixin, View):
    """Help the user manage his data
    """
    def get(self, request, *args, **kwargs):
        current_user = self.request.user

        # There are cases where the user has
        # no connected accounts. In which case,
        # we get an error that no query exists
        try:
            # Query the social_auth database and
            # get a set of connected accounts
            user = self.request.user.social_auth.get(uid=current_user.email)
            if user:
                context = {
                    'provider': user.provider
                }
        except Exception:
            context = {}

        return render(request, 'accounts/pages/data.html', context)


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
        context = {
            'form': NewPaymentMethodForm
        }
        return render(request, 'accounts/pages/payment_methods.html', context)

    def post(self, request, *kwargs):
        try:
            import stripe
        except ImportError:
            raise Http404('An error has occured')
        else:
            # We can update the customer's cards here
            # using the stripe api
            params = {
                'description': 'description'
            }
            customer = stripe.Customer.update(**params)
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
