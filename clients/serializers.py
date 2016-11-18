from rest_framework.serializers import ModelSerializer

from clients.models import Client, ClientContact


class ClientContactSerializer(ModelSerializer):
    class Meta:
        model = ClientContact
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    contacts = ClientContactSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Client
        fields = '__all__'


class InvoiceClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
