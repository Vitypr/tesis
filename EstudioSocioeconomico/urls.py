from django.urls import path

from EstudioSocioeconomico import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name="index"),
    path('navbar/', views.navbar, name="navbar"),
    path('estudio/', views.estudio, name="estudio"),
    path('registro_estudio/', views.registro_estudio, name="reg"),
    path('ver_estudio/', views.ver_estudio, name="ver_estudio"),
    path('prueba_estudio/', views.prueba_estudio, name="prueba_estudio"),
    path('ver_cuota/', views.ver_cuota, name="ver_cuota"),
    path('calcular_cuota/', views.calcular_cuota, name="calcular_cuota"),
    path('prueba/', views.prueba, name="prueba"),
    path('login/', views.login, name="login")
]