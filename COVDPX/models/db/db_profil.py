from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=False)
    friends = models.ManyToManyField(User, related_name="friends")

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profil, on_delete=models.CASCADE,default=False)


class Commentary(models.Model):
    author = models.ForeignKey(Profil, on_delete=models.CASCADE,default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profil, on_delete=models.CASCADE,default=False)











