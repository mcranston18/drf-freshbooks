from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.permissions import ClientPermission
from clients.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [ClientPermission]

    def get_queryset(self):
        return Client.objects.filter(
            user__id = self.request.user.id
        )
