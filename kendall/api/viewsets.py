from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.serializers import (MYUSER, MyUserProfile, UserProfileSerializer,
                             UserSerializer)


class Users(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = UserSerializer
    queryset = MYUSER.objects.all()
    authentication_classes = []
    permission_classes = []

class UserProfiles(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = UserProfileSerializer
    queryset = MyUserProfile.objects.all()
    authentication_classes = []
    permission_classes = []
