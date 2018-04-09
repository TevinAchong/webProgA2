from django.forms import ModelForm
from django import forms
from .animes import Anime

class animeForm(ModelForm):
    # animeId = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Anime ID'
    #     }
    # ))

    # name = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Name'
    #     }
    # ))

    # genre = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Genre'
    #     }
    # ))

    # animeType = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Type'
    #     }
    # ))

    # episodes = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Episodes'
    #     }
    # ))

    # rating = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Rating'
    #     }
    # ))

    # members = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Members'
    #     }
    # ))

    # imageUrl = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'class' : 'form-control', 
    #         'placeholder'  : 'Image URL'
    #     }
    # ))

    class Meta:
        model = Anime
        #fields = ('animeId', 'name', 'genre', 'episodes', 'rating', 'members', 'imageUrl',)
        exclude = ()


