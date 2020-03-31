from django.db.models import F
from SERVER.models.db.db_profil import Page
import datetime
from django.core.cache import cache
from django.conf import settings



def StatsMiddleware(get_response):
    def middleware(request):
        try:
            p = Page.objects.get(url=request.path)
            p.nb_visits = F('nb_visits') + 1
            p.save()
        except Page.DoesNotExist:
            p = Page.objects.create(url=request.path)
        response = get_response(request)
        return response
    return middleware

