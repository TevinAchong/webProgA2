from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic, Webpage, AccessRecord, User
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}

    return render(request, 'firstApp/index.html', context = date_dict)

def users(request):
    userList = User.objects.order_by('lastName')
    userDict = {'users' : userList}

    return render(request, 'firstApp/users.html', context = userDict)