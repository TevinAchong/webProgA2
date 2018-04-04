from django.db import models

# Create your models here.
class Anime(models.Model):
    animeId = models.CharField(max_length = 100,unique = True) ##Ideally should be unique
    name = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 500)
    animeType = models.CharField(max_length = 500)
    episodes = models.CharField(max_length = 10)
    rating = models.CharField(max_length = 500)
    members = models.CharField(max_length = 500)
    #poster = models.ImageField() ##To store images retrieved by Google Search
    #----All data fields are stored as CharField due to possible inconsistencies in anime.csv file ---#
    

    def __str__(self):
        return str(self.name)