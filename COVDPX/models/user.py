from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
