from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from oauth2_provider.ext.rest_framework import (
    TokenHasReadWriteScope,
    TokenHasScope,
)

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer

    # def retrieve(self, request, pk=None):
    #     queryset = self.get_queryset()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = serializers.UserDetailSerializer(user)
    #     return Response(serializer.data)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.UserListSerializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
