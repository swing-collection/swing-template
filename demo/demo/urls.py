# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Demo URL Patterns
==========================

Defines URL patterns for the demo project. This includes:

- Admin panel routes for managing the application.
- A placeholder for routes contributed by your reusable app.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.contrib import admin
from django.urls import URLPattern, URLResolver, path

# Import | Local Modules


# =============================================================================
# URL Patterns
# =============================================================================

urlpatterns: list[URLPattern | URLResolver] = [
    path("admin/", admin.site.urls),  # Admin site URL
    # Once your app exists under `src/`, wire its URLs in here, e.g.:
    # path("", include("swing_template.urls")),
]
