from .animes import Anime
from django.forms import forms

def search(request,Aname):
    Anime n = Anime.objects.filter(name = Aname)
    if(n):
        return n
    else:
        raise forms.ValidationError("Anime does not exist")
    
            
def 


def update(request, NAME):
    ani = Anime.objects.get(name = NAME)
    ani.name = request.POST.get('name')
    anime.animeId =  request.POST.get('animeId')
    
    anime.name = form.cleaned_data['name']
            anime.genre = form.cleaned_data['genre']
            anime.animeType = form.cleaned_data['animeType']
            anime.episodes = form.cleaned_data['episodes']
            anime.rating = form.cleaned_data['rating']
            anime.members = form.cleaned_data['members']



   emp.save()
   return HttpResponse('updated')
