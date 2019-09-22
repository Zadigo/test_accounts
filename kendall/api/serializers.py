from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer

from accounts.models import MyUserProfile

MYUSER = get_user_model()

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MYUSER
        fields = ['nom', 'prenom', 'email']

class UserProfileSerializer(HyperlinkedModelSerializer):
    myuser = UserSerializer()
    class Meta:
        model = MyUserProfile
        fields = ['adresse', 'myuser']
