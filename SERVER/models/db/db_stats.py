from django.db import models


class Page(models.Model):
    url = models.URLField()
    nb_visits = models.IntegerField(default=1)

    def __str__(self):
        return self.url