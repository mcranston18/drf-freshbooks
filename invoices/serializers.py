from rest_framework.serializers import ModelSerializer

from clients.serializers import InvoiceClientSerializer
from projects.serializers import ProjectSerializer
from .models import Invoice


class InvoiceExpandedSerializer(ModelSerializer):
    client = InvoiceClientSerializer()
    projects = ProjectSerializer(
        many=True
    )

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

    def validate(self, data):
        """
        Ensure all projects on invoice have the same client as the client
        property on the invoice
        """
        for project in data['projects']:
            if project.client != data['client'].id:
                raise rest_framework.serializers.ValidationError('badddd')

        return data
