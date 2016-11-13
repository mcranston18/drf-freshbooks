from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    filter_fields = ('client_type', 'name')

    def get_queryset(self):
        queryset = Client.objects.filter(
            user__id=self.request.user.id
        )

        return queryset
