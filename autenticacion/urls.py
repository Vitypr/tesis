from django import views
from django.urls import path

from .views import Vregistro

from EstudioSocioeconomico import views




urlpatterns = [

   path('', views.index, name='home')

   
]
