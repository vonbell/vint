from random import choices
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Vinyl(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release_date = models.DateField('Release Date')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.artist

    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})