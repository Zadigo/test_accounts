from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from accounts.models import MyUser
from accounts.rest_serializers import UserProfileSerializer, UserSerializer


class UserViewSet(ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filtered_queryset = queryset.filter(nom='Test')
        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(data=serializer.data)
