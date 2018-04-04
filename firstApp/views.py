from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Anime
from . import forms
#from bs4 import BeautifulSoup
# Create your views here.

def index(request):
    anime_list = Anime.objects.order_by('name') #--Storing all Anime in a List--#
    anime_dict = {'anime' : anime_list} #---Saving the list as the value in a dictionary to be referenced by the template via the key ---#

    return render(request, 'firstApp/index.html', context = anime_dict)


def form_name_view(request):
    form = forms.animeForm()
    
    #User clicked submit
    if request.method == 'POST': 
        form = forms.animeForm(request.POST)##storing the anime form values in the variable form 

        if form.is_valid():
            print("VALIDATION SUCCESS")
            ##Just printing the values submitted to the command line
            print("id: " +form.cleaned_data['animeID']) 
            print("Name: " +form.cleaned_data['name'])
            print("Genre: " +form.cleaned_data['genre'])
            print("Type: " +form.cleaned_data['Atype'])
            print("Episodes: " +form.cleaned_data['episodes'])
            print("Rating: " +form.cleaned_data['rating'])
            print("Members: " +form.cleaned_data['members'])

    return render(request, 'firstApp/form.html', {'form': form}) ##reloading the form page after submission 
