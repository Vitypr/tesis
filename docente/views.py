import pickle
from tkinter import Entry
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, Template
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from django.urls import reverse
from EstudioSocioeconomico.models import Declaracion, Facultad, Carrera, Estudiantes, Contacto_Estudiante, Propiedades, Grupo_familiare, Educacion_Familia, Bienes_Familiare, Usuario, datos_economicos_familia, Referencia, Recibos, datos_neurona

# Create your views here.

@login_required
def docente(request):
    user= request.user
    users= user.id
    estudiante= Estudiantes.objects.values().filter(usuario_id=user.id)
    estudiantes= Estudiantes.objects.select_related("usuario")
    page= "index"
    return render(request, "docente.html", {"page":page, "user":user, "users":users, "estudiantes":estudiantes})

@login_required
def estudio_docente(request):
    id= request.GET['id']
    estudiante= Estudiantes.objects.values().filter(usuario_id=id)
    contacto_estudiante= Contacto_Estudiante.objects.values().filter(usuario_id=id)
    carrera= Carrera.objects.values().filter(usuario_id=id)
    referencia= Referencia.objects.values().filter(usuario_id=id)
    grupo_familiar= Grupo_familiare.objects.values().filter(usuario_id=id)
    educacion= Educacion_Familia.objects.values().filter(usuario_id=id)
    bienes= Bienes_Familiare.objects.values().filter(usuario_id=id)
    economico= datos_economicos_familia.objects.values().filter(usuario_id=id)
    declaracion = Declaracion.objects.values().filter(usuario_id=id)
    page= "estudio"
    groups = Group.objects.values_list().filter(user=request.user)[0][1]
    return render(request, "estudio_docente.html", {"id":id, "page":page, "estudiante":estudiante, "contacto_estudiante":contacto_estudiante, "carrera":carrera,
    "referencia":referencia, "grupo_familiar":grupo_familiar, "educacion":educacion, "bienes":bienes, "economico":economico, "groups":groups, "declaracion":declaracion})

@login_required
def update_estudio(request):
    id = request.POST['id']
    observaciones = request.POST['observaciones']
    economico_u = datos_economicos_familia.objects.get(usuario_id=id)
    economico_u.observaciones = observaciones
    economico_u.save()
    return HttpResponseRedirect(reverse('docente'))


@login_required
def cuota(request):
    page= "estudio"
    user= request.user
    id= request.GET['id']
    groups = Group.objects.values_list().filter(user=request.user)[0][1]
    cuota = datos_neurona.objects.values().filter(usuario_id=id)
    return render(request, "cuota.html", {"page":page, "groups":groups, "cuota":cuota, "id":id})

def actualizar_cuota(request):
    id = request.POST['id']
    cuota_estudiante = request.POST['cuota_estudiante']
    cuota = datos_neurona.objects.get(usuario_id=id)
    cuota.cuota_estudiante = cuota_estudiante
    cuota.save()

    estudiante=Estudiantes.objects.get(usuario_id=id)
    estudiante.estado = "3"
    estudiante.save()

    return HttpResponseRedirect(reverse('docente'))
