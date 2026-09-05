"""Minimal URLConf for test Django project."""

from django.contrib import admin
from django.urls import URLPattern, URLResolver, path

urlpatterns: list[URLPattern | URLResolver] = [
    path("admin/", admin.site.urls),
]
