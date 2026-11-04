"""
Django settings for the portfolio site.

The site is intentionally database-free so it can run on read-only
serverless platforms (Vercel, Netlify Functions, AWS Lambda) with no
external services attached. All page content lives in
``portfolio/content.py``.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def env_bool(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def env_list(name: str, default: str = "") -> list[str]:
    raw = os.environ.get(name, default)
    return [item.strip() for item in raw.split(",") if item.strip()]


# --------------------------------------------------------------------------
# Core
# --------------------------------------------------------------------------

# A real secret is only needed for signing (CSRF). Set SECRET_KEY in the
# hosting provider's environment variables for production.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-only-key-change-me-in-production-0f3a9c21d7b4",
)

DEBUG = env_bool("DEBUG", default=False)

# Vercel injects VERCEL_URL with the current deployment's hostname.
ALLOWED_HOSTS = env_list("ALLOWED_HOSTS", ".vercel.app,localhost,127.0.0.1")
if vercel_url := os.environ.get("VERCEL_URL"):
    ALLOWED_HOSTS.append(vercel_url)
if DEBUG:
    ALLOWED_HOSTS.append("*")

CSRF_TRUSTED_ORIGINS = [
    f"https://*{host}" if host.startswith(".") else f"https://{host}"
    for host in ALLOWED_HOSTS
    if host not in {"*", "localhost", "127.0.0.1"}
]

# Honour the proxy's protocol header so request.is_secure() is correct
# behind Vercel's edge network.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# --------------------------------------------------------------------------
# Applications
# --------------------------------------------------------------------------
# No admin / auth / sessions: the site has no database and no logged-in
# users, so those apps would only add unused migrations and middleware.
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "portfolio",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "portfolio.context_processors.site_context",
            ],
        },
    },
]

# Explicitly empty: nothing in the project touches a database.
DATABASES = {}

# --------------------------------------------------------------------------
# Internationalisation
# --------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Karachi")
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------
# Static files
# --------------------------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}

# Serve static assets straight through the staticfiles finders. This means
# the serverless deployment works without a `collectstatic` build step and
# without a writable filesystem.
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = DEBUG
WHITENOISE_MAX_AGE = 0 if DEBUG else 31536000

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------------------------------
# Contact form delivery
# --------------------------------------------------------------------------
# Optional. With no SMTP environment variables set, the contact form still
# validates and responds, and the message is written to the application log
# instead of being emailed (see portfolio/views.py).
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = env_bool("EMAIL_USE_TLS", default=True)
EMAIL_TIMEOUT = 10
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER or "no-reply@localhost")
CONTACT_EMAIL_BACKEND_READY = bool(EMAIL_HOST and EMAIL_HOST_USER and EMAIL_HOST_PASSWORD)
EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
    if CONTACT_EMAIL_BACKEND_READY
    else "django.core.mail.backends.console.EmailBackend"
)

# --------------------------------------------------------------------------
# Security hardening (active when DEBUG is off)
# --------------------------------------------------------------------------
if not DEBUG:
    # Safe because SECURE_PROXY_SSL_HEADER above tells Django what the edge
    # already terminated; without it this would cause a redirect loop.
    SECURE_SSL_REDIRECT = env_bool("SECURE_SSL_REDIRECT", default=True)
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    X_FRAME_OPTIONS = "DENY"
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}
