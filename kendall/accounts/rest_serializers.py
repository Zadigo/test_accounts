from rest_framework.serializers import HyperlinkedModelSerializer
from accounts.models import MyUser, MyUserProfile

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'nom', 'prenom']

class UserProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = MyUserProfile
        fields = ['addresse']