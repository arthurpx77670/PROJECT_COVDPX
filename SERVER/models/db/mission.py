from django.db import models
from SERVER.models.db.post import Commentary, Post
from django.utils import timezone



class Mission(models.Model):
    date = models.DateTimeField(default=timezone.now)
    proposition = models.OneToOneField(Post, on_delete=models.CASCADE)
    accept = models.OneToOneField(Commentary, on_delete=models.CASCADE)
    # false display, true is in a result
    description = models.BooleanField(default=False)


class Result(models.Model):
    mark = models.IntegerField(null=True)
    opinion = models.TextField(null=True)
    mission = models.OneToOneField(Mission, on_delete=models.CASCADE)
    file = models.FileField(upload_to="result/")

