"""
Module that defines the models of the music app
"""

from django.db import models


class Songs(models.Model):
    """
    Songs model class that defines the Songs database table
    """
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)
