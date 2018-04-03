from django import forms 
from django.core import validators
from .models import Anime

class animeForm(forms.Form):
    animeID = forms.CharField()
    name = forms.CharField()
    genre = forms.CharField()
    Atype = forms.CharField()
    episodes = forms.CharField()
    rating = forms.CharField()
    members = forms.CharField()

    def clean(self):
        all_clean = super().clean()
        aID = all_clean['animeID']

"""        try:
            p = Anime.objects.get(animeId = aID)
            if p:
                raise forms.ValidationError("Anime with that ID already exists")
        except:
            """

