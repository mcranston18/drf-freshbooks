from django.contrib.auth.models import User, Group

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from oauth2_provider.ext.rest_framework import (
    TokenHasReadWriteScope,
    TokenHasScope,
)

from .serializers import UserListSerializer, UserDetailSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def list(self):
        queryset = self.get_queryset()
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
