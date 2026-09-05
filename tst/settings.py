# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Django settings for tests / type-checking.

Minimal settings module for this template repo. It intentionally installs
only Django's own contrib apps, since swing-template ships no reusable app
of its own. Once a real app is added under `src/`, list it in
`INSTALLED_APPS` below (see the sibling swing-* repos for the pattern).
"""

# Import | Standard Library
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "test"
DEBUG = True
USE_TZ = True
TIME_ZONE = "UTC"

INSTALLED_APPS: list[str] = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Add your reusable app here once it exists under `src/`, e.g.:
    # "swing.template.apps.SwingTemplateConfig",
]

MIDDLEWARE: list[str] = []

ROOT_URLCONF = "tst.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "staticfiles")
MEDIA_URL = "/media/"
MEDIA_ROOT = "/tmp/swing_test_media"
