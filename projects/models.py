from django.db import models

from clients.models import Client


class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ]

    client = models.ForeignKey(Client)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    start_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    budget = models.IntegerField()

    def __str__(self):
        return self.title
