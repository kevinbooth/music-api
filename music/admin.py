"""
Module for admin specific logic
"""

from django.contrib import admin
from .models import Songs

admin.site.register(Songs)
