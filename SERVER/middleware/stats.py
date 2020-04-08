from django.db.models import F
from SERVER.models.db.stats import Page


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

