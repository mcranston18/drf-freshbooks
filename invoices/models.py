from django.db import models

from clients.models import Client
from projects.models import Project


class Invoice(models.Model):
    name = models.CharField(max_length=500)
    client = models.ForeignKey(Client)
    projects = models.ManyToManyField(
        Project,
        related_name='invoices'
    )
    date_of_issue = models.DateField()
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    tax_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    attachments = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True,
    )
    comment = models.CharField(
        max_length=500,
        blank=True,
    )
    terms = models.CharField(
        max_length=5000,
        blank=True,
    )

    @property
    def total_amount(self):
        tax_amount = (self.tax_rate / self.amount) * 100
        return self.amount + tax_amount

    def __str__(self):
        return self.name
