from django.contrib import admin
from .anime import Anime
# Register your models here.


#Registering all created models so that they can be accessed via the django admin page
admin.site.register(Anime)