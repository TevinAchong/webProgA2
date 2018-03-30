import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject.settings')
import django 
django.setup()
from firstApp.models import Anime


#-- Adding Anime Entries to the SQLite DB --#
def populateAnime():
    with open('anime.csv', encoding = 'utf-8') as a: #Retrieving data from anime.csv file....declaring utf-8 so it can be manipulated as desired
        animeReader = csv.reader(a)
        rowCount = 0 ##----Counter to ignore header section of anime.csv file---##
        for row in animeReader:
            if rowCount != 0:
                a = Anime.objects.get_or_create(animeId = row[0], name = row[1], genre = row[2], animeType = row[3], episodes = row[4], rating = row[5], members = row[6])[0]
                a.save() ##Saving Anime Object to database
                print(row) #--Just as a reference to see where the process has reached

            rowCount += 1 #---Moving past the anime.csv header
            
            
            #####-------------------------------------Doing Google Search for Images-----------------------------------#######
            #####-----------------------------------------------------------------------------------------------------#######


if __name__ == '__main__':
    print("Adding anime to Database....")
    populateAnime()


    















