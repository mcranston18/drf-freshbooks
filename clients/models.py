from django.db import models
from django.conf import settings

class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ('startup', 'Startup'),
        ('small', 'Small Business'),
    ]

    name = models.CharField(max_length=30)
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name
