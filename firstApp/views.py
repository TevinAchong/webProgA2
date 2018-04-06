from django.shortcuts import render
from django.http import HttpResponseRedirect
from .anime import Anime
from .anime import animeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate
from django import forms
from django.contrib import messages
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger ##Importing Modules for Pagination


def index(request):
    anime_list = Anime.objects.order_by('name') #--Storing all Anime in a List--#
    
    #---Trying Pagination---#
    
    # page = request.GET.get('page', 1)

    # paginator = Paginator(anime_list, 30)
    # try:
    #     animes = paginator.page(page)
    # except PageNotAnInteger:
    #     animes = paginator.page(1)
    # except EmptyPage:
    #     animes = paginator.page(paginator.num_pages)


    paginator = Paginator(Anime.objects.all(), 30)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    
    try:
        animes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        animes = paginator.page(1)
    
    # Get the index of the current page
    index = animes.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 1 if index >= 3 else 0
    end_index = index + 7 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns 
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    

    return render(request, 'firstApp/index.html', {'anime' : animes, 'page_range' : page_range,})




def search(request):        
    if request.method == 'POST':      


        anime_name = request.POST.getlist('search')
        #anime_name =  request.GET.getlist('search')
        print(anime_name[0])     
        try:
            status = Anime.objects.filter(name__icontains = anime_name[0])
        except Anime.DoesNotExist:
            status = None
        return render(request,"firstApp/search.html", {"animesSearch" : status})


    else:
        return render(request,"firstApp/404.html", {})   
    
    



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

    return render(request, 'firstApp/form.html', {'form': form}) ##reloading the form page after submission 




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    
    else:
        form = UserCreationForm()

        args = {'form':form}
        return render(request, 'firstApp/register.html', args)




def viewAnime(request):
    aId = request.POST.get('anime')
    print(aId)     
    status = Anime.objects.filter(animeId = aId)
    return render(request,"firstApp/details.html", {"animeObj" : status})




def login_view(request):
 
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid:
            userna = request.POST['username']
            passwo = request.POST['password']
            user = authenticate(username = userna, password = passwo)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalid user")
    else:
        form = AuthenticationForm()
            
    return render(request, 'firstApp/login.html', {'form': form} )






