from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.viewsets import ModelViewSet

from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer
    # queryset = Invoice.objects.all()

    def get_queryset(self):
        # user_id = invoice.clients.user
        queryset = Invoice.objects.filter(
            client__user__id=self.request.user.id
        )

        return queryset
