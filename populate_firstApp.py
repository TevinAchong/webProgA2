import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstProject.settings')


import django 
django.setup()

## FAKE POPULATION SCRIPT
import random
from firstApp.models import AccessRecord, Webpage, Topic, User, Anime
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def addTopic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        #get topic for the entry
        top = addTopic()

        #Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        #Create the new webpage entry 
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        #Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]


#-------Populating Users ------#

def populateUser(N = 10):

    for entry in range(N):
        u = User.objects.get_or_create(firstName = fakegen.name(), lastName = fakegen.name(), email = fakegen.email())[0]
        u.save()

#--------------------------------#


def addAnime():
    with open('anime.csv', encoding = 'utf-8') as a:
        animeReader = csv.reader(a)
        for row in animeReader:
            a = Anime.objects.get_or_create(animeId = row[0], name = row[1], genre = row[2], animeType = row[3], rating = row[3], members = row[4])[0]
            a.save()
            print(row)
    


if __name__ == '__main__':
    #print("Populating script....")
    #populate(20)
    #print("Populating Completed!")
    #n = 50
    #populateUser(n)
    #print("Populating Users....")
    #print(str(n) + " users added!")

    addAnime()















