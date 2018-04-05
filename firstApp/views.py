from django.shortcuts import render
from django.http import HttpResponseRedirect
from .anime import Anime
from .anime import animeForm
from django.contrib.auth.forms import UserCreationForm
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

# def viewAnime(request):
#     args = {'user': request.user}
#     return render(request, 'firstApp/animePage.html', args)

# def editAnime(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('firstApp/animePage.html')
#     else:
#         form = UserChangeForm(instance=request.user)
#         args = {'form': form }
#         return render(request, 'firstApp/animePage.html', args)

