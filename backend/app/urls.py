"""
URL configuration for app application.
"""

from django.contrib import admin
from django.urls import include, path

from .api import api


urlpatterns = [
    path('api/', api.urls),
]
