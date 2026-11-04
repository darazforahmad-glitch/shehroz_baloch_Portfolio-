"""WSGI entrypoint.

`application` is the standard Django name; `app` is the alias Vercel's
Python runtime looks for.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

_django_app = get_wsgi_application()

# Some serverless platforms invoke the function with the *destination* path
# of their rewrite rule rather than the URL the visitor asked for, so every
# request arrives looking like "/api/index" and nothing matches the URLconf.
# Normalising here keeps routing correct whichever way the host behaves.
_ENTRYPOINT_PATHS = ("/api/index.py", "/api/index")


def application(environ, start_response):
    path = environ.get("PATH_INFO", "")

    for prefix in _ENTRYPOINT_PATHS:
        if path == prefix:
            path = "/"
            break
        if path.startswith(prefix + "/"):
            path = path[len(prefix):]
            break

    # An empty PATH_INFO means the site root; Django's resolver needs the
    # leading slash to match the "" route.
    environ["PATH_INFO"] = path or "/"

    return _django_app(environ, start_response)


app = application
