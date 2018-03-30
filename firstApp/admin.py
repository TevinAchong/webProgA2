from django.contrib import admin
from firstApp.models import Anime
# Register your models here.


#Registering all created models so that they can be accessed via the django admin page
admin.site.register(Anime)