from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.managers import MyUserManager

# #####################
#       USER MODEL
# #####################

class MyUser(AbstractBaseUser):
    """Base user model
    """
    email       = models.EmailField(verbose_name=_('Addresse email'), max_length=255, unique=True,)
    nom         = models.CharField(max_length=100, null=True, blank=True)
    prenom      = models.CharField(max_length=100, null=True, blank=True)
    
    is_active        = models.BooleanField(default=True)
    admin            = models.BooleanField(default=False)
    staff            = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD      = 'email'
    REQUIRED_FIELDS     = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.staff

    @property
    def is_staff(self):
        return self.staff

class MyUserProfile(models.Model):
    """Base user profile model
    """
    myuser              = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # avatar              = models.ImageField(verbose_name='Avater', width_field=50, height_field=50)
    stripe_id           = models.CharField(max_length=100, blank=True, null=True)
    date_naissance      = models.DateField(default=timezone.now, blank=True, null=True)
    # telephone_validator = RegexValidator(regex=r'\+\d+0?\d+{4, 6}', message='Invalid number')
    telephone           = models.CharField(max_length=11, blank=True, null=True)
    adresse             = models.CharField(max_length=150, blank=True, null=True)
    ville               = models.CharField(max_length=100, blank=True, null=True)
    code_postal         = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.myuser.email


# #####################
#       TOKENS
# #####################

class AccountsToken(models.Model):
    token       = models.CharField(default='erzezeuieuo', max_length=15)
    for_user    = models.PositiveIntegerField(blank=True, null=True)
    expiry_date = models.DateField(default=timezone.now)
    created_on  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.token


# #####################
#       SIGNALS
# #####################

@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MyUserProfile.objects.create(myuser=instance)
