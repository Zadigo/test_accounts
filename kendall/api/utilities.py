from django.apps import apps as django_apps
from django.conf import settings

def get_user_profile_model():
    """
    Return the User profile model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.AUTH_USER_PROFILE_MODEL, require_ready=False)
    except ValueError:
        print('[ACCOUNTS]: User profile model not in accounts \
                or did you forget to register it in settings?')
    except LookupError:
        print('[ACCOUNTS]: User profile model not in accounts \
                or did you forget to register it in settings?')
