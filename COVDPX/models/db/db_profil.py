from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=False)
    friends = models.ManyToManyField(User, related_name="friends")

