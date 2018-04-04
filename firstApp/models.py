from django.db import models
<<<<<<< HEAD
from .anime import Anime
=======

# Create your models here.
class Anime(models.Model):
    animeId = models.CharField(max_length = 100, unique = True) ##Ideally should be unique
    name = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 500)
    animeType = models.CharField(max_length = 500)
    episodes = models.CharField(max_length = 10)
    rating = models.CharField(max_length = 500)
    members = models.CharField(max_length = 500)
    imageUrl = models.CharField(max_length = 500)
    #poster = models.ImageField() ##To store images retrieved by Google Search
    #----All data fields are stored as CharField due to possible inconsistencies in anime.csv file ---#
    
    def __str__(self):
        return str(self.name)

    
>>>>>>> 17c1c9b120ab02698df9365d6a43677dcdf53045
