from django.urls import path
from firstApp import views
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout

urlpatterns = [
    path(r'', views.index, name='index'),

]