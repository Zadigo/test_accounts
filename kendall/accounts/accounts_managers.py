from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import GroupManager




# #####################
#   ACCOUNTS MANAGER
# #####################

class MyUserManager(BaseUserManager):
    def create_user(self, email, nom=None, prenom=None, username=None, password=None):
        """Create a basic user for your application.
        """
        if not email:
            raise ValueError(_("L'addresse mail est obligatoire"))

        user = self.model(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
        )
        
        user.set_password(password)
        user.save(using=self._db)

        return user

    # def create_user_x(self, email, nom=None, prenom=None, password=None, candidat=True):
    #     if not email:
    #         raise ValueError(_("L'addresse mail est obligatoire"))

    #     user = self.model(
    #         email=self.normalize_email(email),
    #         nom=nom,
    #         prenom=prenom,
    #     )

    #     user.candidat=candidat
    #     user.set_password(password)
    #     user.save(using=self._db)

    #     return user

    def create_superuser(self, email, password, nom=None, prenom=None):
        """Create a superuser of type administrator
        """
        user = self.create_user(
            email,
            password=password,
            nom=nom,
            prenom=prenom,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        
        return user
        