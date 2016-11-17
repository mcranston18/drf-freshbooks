from django.db import models
from django.conf import settings


class ClientContact(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        help_text='The name of the contact associated with the client'
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        help_text='The e-mail of the contact associated with the client'
    )


class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ('startup', 'Startup'),
        ('small', 'Small Business'),
    ]

    name = models.CharField(max_length=30)
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    contacts = models.ForeignKey(
        ClientContact,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
