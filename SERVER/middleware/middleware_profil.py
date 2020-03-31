import datetime
from django.core.cache import cache
from django.conf import settings


def ActiveUserMiddleware(get_response):
    def middleware(request):
        current_user = request.user
        if request.user.is_authenticated:
            now = datetime.datetime.now()
            cache.set('seen_%s' % (current_user.username), now, settings.USER_LAST_SEEN_TIMEOUT)
        response = get_response(request)
        return response
    return middleware