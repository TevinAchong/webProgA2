from django.shortcuts import render
from django.http import HttpResponseRedirect
from .anime import Anime
from .anime import animeForm
# Create your views here.

def index(request):
    anime_list = Anime.objects.order_by('name') #--Storing all Anime in a List--#
    anime_dict = {'anime' : anime_list} #---Saving the list as the value in a dictionary to be referenced by the template via the key ---#

    return render(request, 'firstApp/index.html', context = anime_dict)


def form_name_view(request):
    form = animeForm()
    
    if request.method == 'POST':
        form = animeForm(request.POST)

        if form.is_valid():
            anime = Anime()
            anime.animeId =  form.cleaned_data['animeId']
            anime.name = form.cleaned_data['name']
            anime.genre = form.cleaned_data['genre']
            anime.animeType = form.cleaned_data['animeType']
            anime.episodes = form.cleaned_data['episodes']
            anime.rating = form.cleaned_data['rating']
            anime.members = form.cleaned_data['members']

            form.save()
            return HttpResponseRedirect("/")

    return render(request, 'firstApp/form.html', {'form': form})
