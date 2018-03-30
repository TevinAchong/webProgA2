from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Anime
# Create your views here.

def index(request):
    anime_list = Anime.objects.order_by('name') #--Storing all Anime in a List--#
    anime_dict = {'anime' : anime_list} #---Saving the list as the value in a dictionary to be referenced by the template via the key ---#

    return render(request, 'firstApp/index.html', context = anime_dict)
