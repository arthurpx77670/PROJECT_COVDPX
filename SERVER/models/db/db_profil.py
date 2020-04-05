from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.cache import cache
import datetime
from PROJECT_COVDPX import settings


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=False)
    friends = models.ManyToManyField(User, related_name="friends")
    picture = models.ImageField(upload_to="picture/", default=False)

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


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profil, on_delete=models.CASCADE,default=False)
    file = models.FileField(upload_to="file/", default=False)



class Commentary(models.Model):
    author = models.ForeignKey(Profil, on_delete=models.CASCADE,default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profil, on_delete=models.CASCADE,default=False)


class Chat(models.Model):
    sender = models.ForeignKey(Profil, on_delete=models.CASCADE, default=False, related_name="sender")
    receiver = models.ForeignKey(Profil, on_delete=models.CASCADE, default=False,related_name="receiver")
    text = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)


# migrate db_stat
class Page(models.Model):
    url = models.URLField()
    nb_visits = models.IntegerField(default=1)

    def __str__(self):
        return self.url











