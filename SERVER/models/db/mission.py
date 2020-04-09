from django.db import models
from SERVER.models.db.post import Commentary, Post


class Mission(models.Model):
    proposition = models.OneToOneField(Post, on_delete=models.CASCADE)
    accept = models.OneToOneField(Commentary, on_delete=models.CASCADE)
    # false display, true is in a result
    description = models.BooleanField(default=False)


class Result(models.Model):
    mark = models.IntegerField(null=True)
    opinion = models.TextField(null=True)
    mission = models.OneToOneField(Mission, on_delete=models.CASCADE)
    file = models.FileField(upload_to="result/")

