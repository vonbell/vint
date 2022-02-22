from django.forms import ModelForm
from .models import Vinyl, Photo

class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = ('artist', 'album', 'release_date', 'genre', 'description')

# class PhotoForm(ModelForm):
#     class Meta:
#         model = Photo
#         fields = ('url')
