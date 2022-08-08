from django.urls import path

from docente import views

urlpatterns = [
    path('', views.docente, name="docente"),
    path('estudio_docente/', views.estudio_docente, name="estudio_docente"),
    path('cuota/', views.cuota, name="cuota"),
    path('update_estudio/', views.update_estudio ),
    path('actualizar_cuota/', views.actualizar_cuota)
    
    

]