from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Profil(models.Model):
    user = User

    def __str__(self):
        return "Profil de {0}".format(self.user.username)


