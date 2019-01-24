from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (AuthenticationForm,
                                       ReadOnlyPasswordHashField)
from django.forms import CharField, EmailField
from django.forms.widgets import EmailInput, PasswordInput, TextInput
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from accounts.models import MyUser, MyUserProfile



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))

        return password2

    def save(self, commit=True):
        # Save the provided password 
        # in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
        
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserLoginForm(AuthenticationForm):
    username=EmailField(widget=EmailInput(attrs={'placeholder': 'Email professionnel'}))
    password = forms.CharField(strip=False, widget=PasswordInput(attrs={'placeholder': _('Mot de passe')}))
    
    def clean2(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is None and password:
            raise forms.ValidationError(_("Veuillez entrer un email ainsi qu'un mot de passe"))     

        return self.cleaned_data

class UserSignupForm(forms.Form):
    nom         = CharField(widget=TextInput(attrs={'placeholder': _('Joe')}))
    prenom      = CharField(widget=TextInput(attrs={'placeholder': _('Doe')}))
    email       = EmailField(widget=EmailInput(attrs={'placeholder': _('johndoe@gmail.com')}))
    password    = CharField(widget=PasswordInput(attrs={'placeholder': _('johndoe')}))




# #####################
#   Profile forms
# #####################

class BaseProfileForm(forms.ModelForm):
    class Meta:
        model   = MyUser
        fields  = ['nom', 'prenom']
        widgets = {
            'nom': TextInput(attrs={'placeholder': 'John'}),
            'prenom': TextInput(attrs={'placeholder': 'Doe'}),
        }

class AddressProfileForm(forms.ModelForm):
    class Meta:
        model   = MyUserProfile
        fields  = ['adresse', 'ville', 'code_postal']
        widgets = {
            'adresse': TextInput(attrs={'placeholder': '173 rue de Rivoli'}),
            'ville': TextInput(attrs={'placeholder': 'Paris'}),
            'code_postal': TextInput(attrs={'placeholder': '59120'})
        }
