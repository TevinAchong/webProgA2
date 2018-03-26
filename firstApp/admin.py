from django.contrib import admin
from firstApp.models import AccessRecord, Topic, Webpage, User, Anime
# Register your models here.


#Registering all created models so that they can be accessed via the django admin page
admin.site.register(AccessRecord) 
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
admin.site.register(Anime)