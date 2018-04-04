<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .anime import Anime
from .anime import animeForm
=======
from django.shortcuts import render, render_to_response
import django.template
import django.http
from django.http import HttpResponse
from firstApp.models import Anime
from . import forms
#from bs4 import BeautifulSoup
>>>>>>> 17c1c9b120ab02698df9365d6a43677dcdf53045
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger ##Importing Modules for Pagination

def index(request):
    anime_list = Anime.objects.order_by('name') #--Storing all Anime in a List--#
    
    #---Trying Pagination---#
    
    page = request.GET.get('page', 1)

    paginator = Paginator(anime_list, 30)
    try:
        animes = paginator.page(page)
    except PageNotAnInteger:
        animes = paginator.page(1)
    except EmptyPage:
        animes = paginator.page(paginator.num_pages)

    #anime_dict = {'anime' : anime_list} #---Saving the list as the value in a dictionary to be referenced by the template via the key ---#

    return render(request, 'firstApp/index.html', {'anime' : animes})




def search(request):        
    if request.method == 'GET':      
        anime_name =  request.GET.getlist('search')      
        try:
            status = Anime.objects.filter(name__icontains = anime_name)
        except Anime.DoesNotExist:
            status = None
        return render(request,"firstApp/index.html", {"animesSearch" : status})
    else:
        return render(request,"firstApp/index.html",{})   
    
    
def form_name_view(request):
    form = animeForm()
    
<<<<<<< HEAD
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
=======
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
>>>>>>> 17c1c9b120ab02698df9365d6a43677dcdf53045

    return render(request, 'firstApp/form.html', {'form': form}) ##reloading the form page after submission 
