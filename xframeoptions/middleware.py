from django.conf import settings
from django.http import HttpResponse

class Header(object):

    def process_response(self, request, response):
        """Append an X-Frame-Options output header to responses."""
        options = getattr(settings, 'X_FRAME_OPTIONS', 'DENY')
        response['X-FRAME-OPTIONS'] = options.upper()
        return response
