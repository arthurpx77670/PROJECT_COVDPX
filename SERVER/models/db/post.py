from django.db import models
from django.utils import timezone
from SERVER.models.db.profile import Profile


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,default=False)
    file = models.FileField(upload_to="file/", default=False)
    price = models.IntegerField(null=True)
    deadline = models.DateField(null=True)
    # false display, true is in a mission
    description = models.BooleanField(default=False)


class Commentary(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    price = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)
    # false display, true is in a mission
    description = models.BooleanField(default=False)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,default=False)


