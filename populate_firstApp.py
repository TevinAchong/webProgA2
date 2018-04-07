"""

This script contains the various functions used to populate the database

"""



import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject.settings')
import django 
django.setup()
from firstApp.models import Anime
from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen, Request
from http.cookiejar import CookieJar
import json

def get_soup(url,header):
    return BeautifulSoup(urlopen(Request(url,headers=header)),'html.parser')

def addImageURL(animeName):
    if animeName.isalnum():
        query = animeName
    else:
        query = re.sub('[^A-Za-z0-9]+', '', animeName)
    # you can change the query for the image  here
    print('Query: ',query)
    image_type="ActiOn"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    #print(url)
    
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    try:
        soup = get_soup(url,header)
        a = soup.find("div",{"class":"rg_meta"})
        link = json.loads(a.text)["ou"]
        #Type =  json.loads(a.text)["ity"]
        ActualImage = (link)  #contains the link for Large original images, type of  image

        print(ActualImage)
        return (ActualImage)

    except:
        return '{\%\static "images/placeholder.png" %}'



#-- Adding Anime Entries to the SQLite DB --#
def populateAnime():
    with open('anime.csv', encoding = 'utf-8') as a: #Retrieving data from anime.csv file....declaring utf-8 so it can be manipulated as desired
        animeReader = csv.reader(a)
        rowCount = 0 ##----Counter to ignore header section of anime.csv file---##
        for row in animeReader:
            if rowCount != 0:
                a = Anime.objects.get_or_create(animeId = row[0], name = row[1], genre = row[2], animeType = row[3], episodes = row[4], rating = row[5], members = row[6], imageUrl = addImageURL(row[1]))[0]
                a.save() ##Saving Anime Object to database
                print(row) #--Just as a reference to see where the process has reached

            rowCount += 1 #---Moving past the anime.csv header
            

if __name__ == '__main__':
    print("Adding anime to Database....")
    #populateAnime()
    #addImageURL('MÄR')
    # an = Anime.objects.filter(imageUrl = '{%static "images/placeholder.png" %}')
    # for ani in an:
    #     print(ani)
    #     ani.imageUrl = "{%static \"images/placeholder.png\" %}"
    #     ani.save()

    an = Anime.objects.filter(name = 'Monster')
    an[0].imageUrl = 'http://www.misucell.com/data/out/10/IMG_454899.png'
    















