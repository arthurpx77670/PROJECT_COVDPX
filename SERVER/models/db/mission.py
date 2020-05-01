from django.db import models
from SERVER.models.db.post import Commentary, Post
from django.utils import timezone
from SERVER.models.db.profile import Profile

class Mission(models.Model):
    date = models.DateTimeField(default=timezone.now)
    proposition = models.OneToOneField(Post, on_delete=models.CASCADE)
    accept = models.OneToOneField(Commentary, on_delete=models.CASCADE)
    # false display, true is in a result
    description = models.BooleanField(default=False)


class Result(models.Model):
    mission = models.OneToOneField(Mission, on_delete=models.CASCADE)
    winner = models.ForeignKey(Profile, on_delete=models.CASCADE,default=False, related_name="winner")
    looser = models.ForeignKey(Profile, on_delete=models.CASCADE,default=False, related_name="looser")
    # pas opti
    playerConfirm = models.ForeignKey(Profile, on_delete=models.CASCADE,default=False, related_name="playerConfirm")
    conflict = models.BooleanField(default=False)
    description = models.BooleanField(default=False)


