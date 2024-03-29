from random import choices
from django.db import models
from django.urls import reverse

GENRES = (
    ("PP", "Pop"),
    ("RK", "Rock"),
    ("HH", "Hip-Hop"),
    ("FK", "Folk"),
    ("CY", "Country"),
    ("RB", "R&B"),
    ("JZ", "Jazz"),
    ("BL", "Blues"),
    ("CL", "Classical"),
    ("EL", "Electronic"),
    ("DC", "Dance"),
    ("KP", "K-Pop"),
    ("CN", "Christian"),
    ("GO", "Gospel"),
    ("CO", "Comedy"),
    ("OL", "Oldies"),
    ("RG", "Reggae"),
    ("AP", "Afro Pop"),
    ("SO", "Soul"),
    ("AL", "Alternative"),
    ("IE", "Indie"),
    ("WW", "Worldwide"),
)

class Vinyl(models.Model):
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    release_date = models.DateField('Release Date')
    genre = models.CharField(
        max_length=2,
        choices=GENRES,
        default=GENRES[0][0],
    )

    def __str__(self):
        return self.album

    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for vinyl_id: {self.vinyl_id} @{self.url}"
