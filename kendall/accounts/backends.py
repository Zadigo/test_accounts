from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


MYUSER = get_user_model()

class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = MYUSER.objects.get(email=email)
            if user.check_password(password):
                return user
        
        except MYUSER.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MYUSER.objects.get(pk=user_id)
            
        except MYUSER.DoesNotExist:
            return None
