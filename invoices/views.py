from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.viewsets import ModelViewSet

from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        queryset = Invoice.objects.filter(
            client__user__id=self.request.user.id
        )

        return queryset
