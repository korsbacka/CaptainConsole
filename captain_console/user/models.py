from django.contrib.auth.models import User
from django.db import models

from consoles.models import Console


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_console = models.ForeignKey(Console, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
