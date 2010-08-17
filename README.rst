====================
django-xframeoptions
====================

Django application with middleware component that appends ``X-Frame-Options`` output header to responses with a configurable value. It's very, very basic for now. 

Installation
============

Install django-xframeoptions from the git repository: ::

     pip install -e git://github.com/paulosman/django-xframeoptions#egg=xframeoptions

Add django-xframeoptions to your ``INSTALLED_APPS`` in ``settings.py``: ::

     INSTALLED_APPS = (
         ...
         'xframeoptions',
         ...
     )

Add ``xframeoptions.middleware.Header`` to ``MIDDLEWARE_CLASSES`` in ``settings.py``: ::

     MIDDLEWARE_CLASSES = (
         ...
         'xframeoptions.middleware.Header',
         ...
     )

Optionally specify a value for the ``X-Frame-Options`` header in ``settings.py``. Default is ``DENY``: ::

     X_FRAME_OPTIONS = 'SAMEORIGIN'

Usage
=====

Once installed, responses should have an ``X-Frame-Options`` header with the value you specified in ``settings.py`` or ``DENY``: ::

     $ curl -D - http://localhost:8000
     ...
     HTTP/1.0 200 OK
     Date: Tue, 17 Aug 2010 17:56:48 GMT
     Server: WSGIServer/0.1 Python/2.6.5
     Vary: Cookie
     X-FRAME-OPTIONS: DENY
     Content-Type: text/html; charset=utf-8
     Set-Cookie:  csrftoken=670d5c08f178a4104daa4ec34bc5d11c; Max-Age=31449600; Path=
