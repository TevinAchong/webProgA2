#from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate
from django import forms
from django.core import validators

class loginForm(forms.Form):
    username = forms.CharField(max_length=100, required= True)
    password = forms.CharField(widget=forms.PasswordInput, required= True)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid Credentials")
        return self.cleaned_data

    def login(request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        return user
    

    