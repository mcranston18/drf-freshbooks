from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.viewsets import ModelViewSet

from clients.models import Client, ClientContact
from clients.serializers import ClientSerializer, ClientContactSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    filter_fields = ('client_type', 'name')

    def get_queryset(self):
        queryset = Client.objects.filter(
            user__id=self.request.user.id
        )

        return queryset


class ClientContactsViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = ClientContactSerializer
    queryset = ClientContact.objects.all()
