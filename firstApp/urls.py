from django.urls import path
from firstApp import views

urlpatterns = [
    path(r'', views.index, name='index'),
]