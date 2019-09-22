from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer

from api.utilities import get_user_profile_model


MYUSER = get_user_model()

MYUSERPROFILE = get_user_profile_model()

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MYUSER
        fields = ['nom', 'prenom', 'email']

class UserProfileSerializer(HyperlinkedModelSerializer):
    myuser = UserSerializer()
    class Meta:
        model = MYUSERPROFILE
        fields = ['adresse', 'myuser']
