from django.forms import ModelForm
from .animes import Anime

class animeForm(ModelForm):
    class Meta:
        model= Anime
        exclude = ()


