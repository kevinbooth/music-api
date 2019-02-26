"""
Module that handles the serialization of Song data
"""

from rest_framework import serializers
from .models import Songs


class SongsSerializer(serializers.ModelSerializer):
    """
    Songs Serializer class used to map how JSON objects should render.
    """

    class Meta:
        model = Songs
        fields = ("title", "artist")
