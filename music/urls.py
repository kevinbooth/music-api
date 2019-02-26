"""
Module that resolves url paths to a specific view in the music app
"""

from django.urls import path
from .views import ListSongsView

"""
Specifying the url route.
"""
urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
