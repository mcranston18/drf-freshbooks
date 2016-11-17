from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    favourite_colour = models.CharField(
        max_length=30,
        blank=True,
    )
