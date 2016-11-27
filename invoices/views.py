from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Invoice
from .serializers import InvoiceSerializer, InvoiceExpandedSerializer


class InvoiceViewSet(ModelViewSet):
    def get_queryset(self,):
        queryset = Invoice.objects.filter(
            client__user__id=self.request.user.id
        )

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InvoiceExpandedSerializer

        return InvoiceSerializer
