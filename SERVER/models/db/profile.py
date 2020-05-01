from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.cache import cache
import datetime
from PROJECT_COVDPX import settings
from  SERVER.models.db.stats import Page


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=False)
    friends = models.ManyToManyField(User, related_name="friends")
    picture = models.ImageField(upload_to="picture/", default=False)
    level = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    confidence = models.IntegerField(default=100)
    number = models.IntegerField(default=0)
    win = models.IntegerField(default=0)

    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False


class Chat(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, default=False, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, default=False,related_name="receiver")
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)











