from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic, Webpage, AccessRecord, User, Anime
# Create your views here.

def index(request):
    anime_list = Anime.objects.order_by('name')
    anime_dict = {'anime' : anime_list}

    return render(request, 'firstApp/index.html', context = anime_dict)

def users(request):
    userList = User.objects.order_by('lastName')
    userDict = {'users' : userList}

    return render(request, 'firstApp/users.html', context = userDict)