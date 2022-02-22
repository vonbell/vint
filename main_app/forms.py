from django.forms import ModelForm
from .models import Vinyl

class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = ('release_date')