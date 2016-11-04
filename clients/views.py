from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.permissions import ClientPermission
from clients.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [ClientPermission]
