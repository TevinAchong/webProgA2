"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from firstApp import views
from django.conf import settings
from django.contrib.auth.views import logout

urlpatterns = [
    path(r'', views.login_view, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url(r'^formpage/', views.form_name_view, name='form_name'),
    url(r'^search', views.search, name='search'),
    url(r'^home/$', views.index, name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^details/$', views.viewAnime, name='details'),
]
