from .animes import Anime
from django.forms import forms

def search(self,Aname):
    Anime n = Anime.objects.filter(name = Aname)
    if(n):
        return n
    else:
        raise forms.ValidationError("Anime does not exist")
    
            
