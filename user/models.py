from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)

    def save(self, *args, **kwargs) -> None:
        created = self._state.adding

        super().save(*args, **kwargs)

        if created:
            Token.objects.create(user=self)
