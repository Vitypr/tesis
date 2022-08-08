from asyncio.windows_events import NULL
from base64 import b64encode
from tokenize import group
from django.shortcuts import render
from django.urls import reverse
import pandas as pd
import numpy as np
import keras
import math 
import re

# Create your views here.

from django.http import HttpResponse
from tkinter import Entry
from functools import wraps
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from EstudioSocioeconomico.models import Declaracion, Facultad, Carrera, Estudiantes, Contacto_Estudiante, Propiedades, Grupo_familiare, Educacion_Familia, Bienes_Familiare, datos_economicos_familia, Referencia, Recibos, datos_neurona
from django.contrib import messages
from django.contrib.auth.models import User, Group

from Tesis.settings import LOGIN_REDIRECT_URL

def login(request):
    groups = Group.objects.values_list().filter(user=request.user)[0][1]
    if groups =="Estudiante":
        return HttpResponseRedirect(reverse('index'))

    elif groups =="admin":
         return HttpResponseRedirect('../admin')

    elif groups =="empleado":
        return HttpResponseRedirect(reverse('docente'))

    context = {}
    template = "index.html"
    return render(request, template, context)


@login_required
def index(request):
    user= request.user
    users= User.objects.all()
    users_id= user.id
    groups = Group.objects.values_list().filter(user=request.user)[0][1]
    print(users_id)
    estudiante= Estudiantes.objects.values().filter(usuario_id=users_id)
    page = "index"
    return render(request, "index.html", {"page":page, "users":users, "estudiante":estudiante, "groups":groups}) 

@login_required
def navbar(request):
    user= request.user
    return render(request, "navbar.html", {"user":user})



@login_required
def estudio(request):
    groups = Group.objects.values_list().filter(user=request.user)[0][1]
    user= request.user
    id= user.id
    users= User.objects.all()
    economico= datos_economicos_familia.objects.values().filter(usuario_id=user.id)
    page = "estudio"
    return render(request, "estudio.html", {"page":page, "id":id, "economico":economico, "groups":groups})

@login_required
def ver_estudio(request):
    groups = Group.objects.values_list().filter(user=request.user)[0][1]
    user= request.user
    id= user.id
    estudiante= Estudiantes.objects.values().filter(usuario_id=id)
    contacto_estudiante= Contacto_Estudiante.objects.values().filter(usuario_id=id)
    carrera= Carrera.objects.values().filter(usuario_id=id)
    referencia= Referencia.objects.values().filter(usuario_id=id)
    grupo_familiar= Grupo_familiare.objects.values().filter(usuario_id=id)
    educacion= Educacion_Familia.objects.values().filter(usuario_id=id)
    bienes= Bienes_Familiare.objects.values().filter(usuario_id=id)
    economico= datos_economicos_familia.objects.values().filter(usuario_id=id)
    declaracion = Declaracion.objects.values().filter(usuario_id=id)
    page = "estudio"
    return render(request, "ver_estudio.html", {"id":id, "page":page, "estudiante":estudiante, "contacto_estudiante":contacto_estudiante, "carrera":carrera,
    "referencia":referencia, "grupo_familiar":grupo_familiar, "educacion":educacion, "bienes":bienes, "economico":economico, "groups":groups, "declaracion":declaracion})

@login_required
def registro_estudio(request):
    user = request.user

    if request.method=='POST':
        usuario_id=request.POST['usuario_id']
        primer_apellido=request.POST['primer_apellido']
        segundo_apellido=request.POST['segundo_apellido']
        nombre_estudiante=request.POST['nombre_estudiante']
        direccion_exacta=request.POST['direccion_exacta']
        telefono_fijo=request.POST['telefono_fijo']
        celular=request.POST['celular']
        email=request.POST['email']
        vive_en=request.POST['vive_en']
        vive_con=request.POST['vive_con']
        estado_civil=request.POST['estado_civil']
        lugar_nacimiento=request.POST['lugar_nacimiento']
        fecha_nacimiento=request.POST['fecha_nacimiento']
        edad_estudiante=request.POST['edad_estudiante']
        nombre_carrera=request.POST['nombre_carrera']
        tipo_titulo=request.POST['tipo_titulo']
        tipo_ingreso=request.POST['tipo_ingreso']
        medio_referencia=request.POST['medio_referencia']
        nombre_amigo=request.POST['nombre_amigo']
        carrera_amigo=request.POST['carrera_amigo']
        lugar_procedencia=request.POST['lugar_procedencia']
        lugar_procedencia2=request.POST['lugar_procedencia2']
        bachiller_opcion=request.POST['bachiller_opcion']
        bachiller_opcion2=request.POST['bachiller_opcion2']
        ciclo_estudiado=request.POST['ciclo_estudiado']
        ciclo_estudiado2=request.POST['ciclo_estudiado2']
        cuota_pagaba=request.POST['cuota_pagaba']
        cuota_pagaba2=request.POST['cuota_pagaba2']
        pago_cuota=request.POST['pago_cuota']
        pago_cuota2=request.POST['pago_cuota2']
        beca_escuela=request.POST['beca_escuela']
        beca_precio=request.POST['beca_precio']
        cantidad_familiares=request.POST['cantidad_familiares']
        nombre=request.POST['nombre']
        parentesco=request.POST['parentesco']
        edad_familiar=request.POST['edad_familiar']
        profesion=request.POST['profesion']
        lugar_trabajo=request.POST['lugar_trabajo']
        nombre2=request.POST['nombre2']
        parentesco2=request.POST['parentesco2']
        edad_familiar2=request.POST['edad_familiar2']
        profesion2=request.POST['profesion2']
        lugar_trabajo2=request.POST['lugar_trabajo2']
        nombre3=request.POST['nombre3']
        parentesco3=request.POST['parentesco3']
        edad_familiar3=request.POST['edad_familiar3']
        profesion3=request.POST['profesion3']
        lugar_trabajo3=request.POST['lugar_trabajo3']
        nombre4=request.POST['nombre4']
        parentesco4=request.POST['parentesco4']
        edad_familiar4=request.POST['edad_familiar4']
        profesion4=request.POST['profesion4']
        lugar_trabajo4=request.POST['lugar_trabajo4']
        nombre5=request.POST['nombre5']
        parentesco5=request.POST['parentesco5']
        edad_familiar5=request.POST['edad_familiar5']
        profesion5=request.POST['profesion5']
        lugar_trabajo5=request.POST['lugar_trabajo5']
        nombre6=request.POST['nombre6']
        parentesco6=request.POST['parentesco6']
        edad_familiar6=request.POST['edad_familiar6']
        profesion6=request.POST['profesion6']
        lugar_trabajo6=request.POST['lugar_trabajo6']
        nombre7=request.POST['nombre7']
        parentesco7=request.POST['parentesco7']
        edad_familiar7=request.POST['edad_familiar7']
        profesion7=request.POST['profesion7']
        lugar_trabajo7=request.POST['lugar_trabajo7']
        nombre8=request.POST['nombre8']
        parentesco8=request.POST['parentesco8']
        edad_familiar8=request.POST['edad_familiar8']
        profesion8=request.POST['profesion8']
        lugar_trabajo8=request.POST['lugar_trabajo8']
        nombre9=request.POST['nombre9']
        parentesco9=request.POST['parentesco9']
        edad_familiar9=request.POST['edad_familiar9']
        profesion9=request.POST['profesion9']
        lugar_trabajo9=request.POST['lugar_trabajo9']
        nombre10=request.POST['nombre10']
        parentesco10=request.POST['parentesco10']
        edad_familiar10=request.POST['edad_familiar10']
        profesion10=request.POST['profesion10']
        lugar_trabajo10=request.POST['lugar_trabajo10']
        nombre_familiar=request.POST['nombre_familiar']
        grado_educacion=request.POST['grado_educacion']
        centro_estudios=request.POST['centro_estudios']
        cuota=request.POST['cuota']
        responsable_cuota=request.POST['responsable_cuota']
        nombre_familiar2=request.POST['nombre_familiar2']
        grado_educacion2=request.POST['grado_educacion2']
        centro_estudios2=request.POST['centro_estudios2']
        cuota2=request.POST['cuota2']
        responsable_cuota2=request.POST['responsable_cuota2']
        nombre_familiar3=request.POST['nombre_familiar3']
        grado_educacion3=request.POST['grado_educacion3']
        centro_estudios3=request.POST['centro_estudios3']
        cuota3=request.POST['cuota3']
        responsable_cuota3=request.POST['responsable_cuota3']
        propiedad_familia=request.POST['propiedad_familia']
        direccion_propiedad=request.POST['direccion_propiedad']
        n_habitaciones=request.POST['n_habitaciones']
        n_baños=request.POST['n_baños']
        propiedad_familia2=request.POST['propiedad_familia2']
        direccion_propiedad2=request.POST['direccion_propiedad2']
        n_habitaciones2=request.POST['n_habitaciones2']
        n_baños2=request.POST['n_baños2']
        propiedad_familia3=request.POST['propiedad_familia3']
        direccion_propiedad3=request.POST['direccion_propiedad3']
        n_habitaciones3=request.POST['n_habitaciones3']
        n_baños3=request.POST['n_baños3']
        inst_vendedora=request.POST['inst_vendedora']
        cuota_mensual=request.POST['cuota_mensual']
        valor_actual=request.POST['valor_actual']
        inst_vendedora2=request.POST['inst_vendedora2']
        cuota_mensual2=request.POST['cuota_mensual2']
        valor_actual2=request.POST['valor_actual2']
        inst_vendedora3=request.POST['inst_vendedora3']
        cuota_mensual3=request.POST['cuota_mensual3']
        valor_actual3=request.POST['valor_actual3']
        posee_vehiculo=request.POST['posee_vehiculo']
        tipo_vehiculo=request.POST['tipo_vehiculo']
        marca_vehiculo=request.POST['marca_vehiculo']
        año_vehiculo=request.POST['año_vehiculo']
        valor_vehiculo=request.POST['valor_vehiculo']
        tipo_vehiculo2=request.POST['tipo_vehiculo2']
        marca_vehiculo2=request.POST['marca_vehiculo2']
        año_vehiculo2=request.POST['año_vehiculo2']
        valor_vehiculo2=request.POST['valor_vehiculo2']
        cantidad_mueble_sala=request.POST['cantidad_mueble_sala']
        valor_mueble_sala=request.POST['valor_mueble_sala']
        cantidad_mueble_comedor=request.POST['cantidad_mueble_comedor']
        valor_mueble_comedor=request.POST['valor_mueble_comedor']
        cantidad_refri=request.POST['cantidad_refri']
        valor_refri=request.POST['valor_refri']
        cantidad_cocina=request.POST['cantidad_cocina']
        valor_cocina=request.POST['valor_cocina']
        cantidad_horno=request.POST['cantidad_horno']
        valor_horno=request.POST['valor_horno']
        cantidad_licuadora=request.POST['cantidad_licuadora']
        valor_licuadora=request.POST['valor_licuadora']
        cantidad_tv=request.POST['cantidad_tv']
        valor_tv=request.POST['valor_tv']
        cantidad_teatro=request.POST['cantidad_teatro']
        valor_teatro=request.POST['valor_teatro']
        cantidad_sonido=request.POST['cantidad_sonido']
        valor_sonido=request.POST['valor_sonido']
        cantidad_camara=request.POST['cantidad_camara']
        valor_camara=request.POST['valor_camara']
        cantidad_compu=request.POST['cantidad_compu']
        valor_compu=request.POST['valor_compu']
        cantidad_lavadora=request.POST['cantidad_lavadora']
        valor_lavadora=request.POST['valor_lavadora']
        cantidad_secadora=request.POST['cantidad_secadora']
        valor_secadora=request.POST['valor_secadora']
        trabajo_alumno=request.POST['trabajo_alumno']
        salario_alumno=request.POST['salario_alumno']
        descuento_alumno=request.POST['descuento_alumno']
        aporte_liquido=request.POST['aporte_liquido']
        trabajo_mama=request.POST['trabajo_mama']
        salario_mama=request.POST['salario_mama']
        descuento_mama=request.POST['descuento_mama']
        aporte_mama=request.POST['aporte_mama']
        trabajo_papa=request.POST['trabajo_papa']
        salario_papa=request.POST['salario_papa']
        descuento_papa=request.POST['descuento_papa']
        aporte_papa=request.POST['aporte_papa']
        trabajo_remesas=request.POST['trabajo_remesas']
        salario_remesas=request.POST['salario_remesas']
        descuento_remesas=request.POST['descuento_remesas']
        aporte_remesas=request.POST['aporte_remesas']
        trabajo_otros=request.POST['trabajo_otros']
        salario_otros=request.POST['salario_otros']
        descuento_otros=request.POST['descuento_otros']
        aporte_otros=request.POST['aporte_otros']
        cantidad_alimento=request.POST['cantidad_alimento']
        detalles_alimento=request.POST['detalles_alimento']
        cantidad_pago_casa=request.POST['cantidad_pago_casa']
        detalles_pago_casa=request.POST['detalles_pago_casa']
        cantidad_abono_prestamo=request.POST['cantidad_abono_prestamo']
        detalles_abono_prestamo=request.POST['detalles_abono_prestamo']
        cantidad_abono_tarjetas=request.POST['cantidad_abono_tarjetas']
        detalles_abono_tarjetas=request.POST['detalles_abono_tarjetas']
        cantidad_serbasicos=request.POST['cantidad_serbasicos']
        detalles_serbasicos=request.POST['detalles_serbasicos']
        cantidad_educacion=request.POST['cantidad_educacion']
        detalles_educacion=request.POST['detalles_educacion']
        cantidad_transporte=request.POST['cantidad_transporte']
        detalles_transporte=request.POST['detalles_transporte']
        cantidad_combustible=request.POST['cantidad_combustible']
        detalles_combustible=request.POST['detalles_combustible']
        cantidad_ayuda_parientes=request.POST['cantidad_ayuda_parientes']
        detalles_ayuda_parientes=request.POST['detalles_ayuda_parientes']
        cantidad_salud=request.POST['cantidad_salud']
        detalles_salud=request.POST['detalles_salud']
        cantidad_internet=request.POST['cantidad_internet']
        detalles_internet=request.POST['detalles_internet']
        cantidad_cable=request.POST['cantidad_cable']
        detalles_cable=request.POST['detalles_cable']
        cantidad_otros=request.POST['cantidad_otros']
        detalles_otros=request.POST['detalles_otros']
        nombre_aspirante=request.POST['nombre_aspirante']
        firma_aspirante=request.POST['firma_aspirante']
        nombre_responsable=request.POST['nombre_responsable']
        firma_responsable=request.POST['firma_responsable']
        fecha_firmo=request.POST['fecha_firmo']
        

        if vive_en == "Casa propia mayor a 50,000":
            vive_en_n = 4
        elif vive_en == "Casa propia entre 20,000 y 50,000":
            vive_en_n = 3
        elif vive_en == "Casa propia menor a 20,000":
            vive_en_n = 2
        elif vive_en == "Alquiler más de 750":
            vive_en_n = 1
        elif vive_en == "Alquiler menos de 750":
            vive_en_n = 0

        if vive_con == "Grupo Familiar":
            vive_con_n = 3
        elif vive_con == "Padre o Madre":
            vive_con_n = 2
        elif vive_con == "Con abuelos":
            vive_con_n = 1
        elif vive_con == "Solo":
            vive_con_n = 0

        if estado_civil == "Soltero(a)":
            estado_civil_n = 3
        elif estado_civil == "Casado(a)":
            estado_civil_n = 1
        elif estado_civil == "Acompañado(a)":
            estado_civil_n = 0 
        elif estado_civil == "Divorciado(a)":
            estado_civil_n = 2

        if cuota_pagaba == "":
            cuota_pagaba_m = 0
            cuota_pagaba_m = float(cuota_pagaba_m)
        else:
            cuota_pagaba_m = float(cuota_pagaba)

        if cuota_pagaba2 == "": 
            cuota_pagaba_m2 = 0
            cuota_pagaba_m2 = float(cuota_pagaba_m2)
        else:
            cuota_pagaba_m2 = float(cuota_pagaba2)


        pago_cuota_t= cuota_pagaba_m + cuota_pagaba_m2

        if pago_cuota_t >= 500:
            cuota_institucion_n= 4
        elif pago_cuota_t >= 200 and pago_cuota_t <= 499:
            cuota_institucion_n = 3
        elif pago_cuota_t >= 100 and pago_cuota_t <= 199:
            cuota_institucion_n = 2
        elif pago_cuota_t >= 50 and pago_cuota_t <= 99:
            cuota_institucion_n = 1
        elif pago_cuota_t <= 49:
            cuota_institucion_n = 0

        if beca_precio == "":
            beca_precio_m = 0
            beca_precio_m = float(beca_precio_m)
        else:
            beca_precio_m = float(beca_precio)

        if beca_precio_m >= 300:
            beca_n = 3
        elif beca_precio_m >= 100 and beca_precio_m <= 299:
            beca_n = 2
        elif beca_precio_m >= 50 and beca_precio_m <= 99:
            beca_n = 1
        elif beca_precio_m <= 49:
            beca_n = 0

        if cantidad_familiares == "1-3":
            miembros_fam_n = 3
        elif cantidad_familiares == "4-5":
            miembros_fam_n = 2
        elif cantidad_familiares == "6-8":
            miembros_fam_n = 1
        elif cantidad_familiares == "9 o Más":
            miembros_fam_n = 0

        if cuota == "":
            cuota_m = 0
            cuota_m = float(cuota_m)
        else:
            cuota_m = float(cuota)

        if cuota2 == "":
            cuota_m2 = 0
            cuota_m2 = float(cuota_m2)
        else:
            cuota_m2 = float(cuota2)

        egresos_fam = cuota_m + cuota_m2

        if egresos_fam >= 500:
            egresos_n = 4
        elif egresos_fam >= 200 and egresos_fam <= 499:
            egresos_n = 3
        elif egresos_fam >= 100 and egresos_fam <= 199:
            egresos_n = 2
        elif egresos_fam >= 50 and egresos_fam <= 99:
            egresos_n = 1
        elif egresos_fam <= 49:
            egresos_n = 0

        if valor_actual == "":
            valor_actual_m = 0
            valor_actual_m = float(valor_actual_m)
        else:
            valor_actual_m = float(valor_actual)
        
        if valor_actual2 == "":
            valor_actual_m2 = 0
            valor_actual_m2 = float(valor_actual_m2)
        else:
            valor_actual_m2 = float(valor_actual2)
        
        if valor_actual3 == "":
            valor_actual_m3 = 0
            valor_actual_m3 = float(valor_actual_m3)
        else:
            valor_actual_m3= float(valor_actual3)

        valor_propiedades = valor_actual_m + valor_actual_m2 + valor_actual_m3

        if valor_propiedades >= 40001:
            propiedades_n = 3
        elif valor_propiedades >= 5001 and valor_propiedades <= 40000:
            propiedades_n = 2 
        elif valor_propiedades >= 2001 and valor_propiedades <= 5000:
            propiedades_n = 1
        elif valor_propiedades <= 2000:
            propiedades_n = 0

        if valor_vehiculo == "":
            valor_vehiculo_m = 0
            valor_vehiculo_m = float(valor_vehiculo_m)
        else:
            valor_vehiculo_m = float(valor_vehiculo)

        if valor_vehiculo2 == "":
            valor_vehiculo_m2 = 0
            valor_vehiculo_m2 = float(valor_vehiculo_m2)
        else:
            valor_vehiculo_m2 = float(valor_vehiculo2)

        vehiculo_total = valor_vehiculo_m + valor_vehiculo_m2

        if vehiculo_total >= 40001:
            vehiculo_n = 3
        elif vehiculo_total >= 20001 and vehiculo_total <= 40000:
            vehiculo_n = 2
        elif vehiculo_total >= 5001 and vehiculo_total <= 20000:
            vehiculo_n = 3
        elif vehiculo_total <= 5000:
            vehiculo_n = 0

        if valor_mueble_sala == "":
            mueble_m = 0
            mueble_m = float(mueble_m)
        else:
            mueble_m = float(valor_mueble_sala)
        
        if valor_mueble_comedor == "":
            mueble_m2 = 0
            mueble_m2 = float(mueble_m2)
        else:
            mueble_m2 = float(valor_mueble_comedor)
        
        if valor_refri == "":
            mueble_m3 = 0
            mueble_m3 = float(mueble_m3)
        else:
            mueble_m3 = float(valor_refri)

        if valor_cocina == "":
            mueble_m4 = 0
            mueble_m4 = float(mueble_m4)
        else:
            mueble_m4 = float(valor_cocina)
        
        if valor_horno == "":
            mueble_m5 = 0
            mueble_m5 = float(mueble_m5)
        else:
            mueble_m5 = float(valor_horno)
        
        if valor_licuadora == "":
            mueble_m6 = 0
            mueble_m6 = float(mueble_m6)
        else:
            mueble_m6 = float(valor_licuadora)
        
        if valor_tv == "":
            mueble_m7 = 0
            mueble_m7 = float(mueble_m7)
        else:
            mueble_m7 = float(valor_tv)

        if valor_teatro == "":
            mueble_m8 = 0
            mueble_m8 = float(mueble_m8)
        else:
            mueble_m8 = float(valor_teatro)

        if valor_sonido == "":
            mueble_m9 = 0
            mueble_m9 = float(mueble_m9)
        else:
            mueble_m9 = float(valor_sonido)

        if valor_camara == "":
            mueble_m10 = 0
            mueble_m10 = float(mueble_m10)
        else:
            mueble_m10 = float(valor_camara)

        if valor_compu == "":
            mueble_m11 = 0
            mueble_m11 = float(mueble_m11)
        else:
            mueble_m11 = float(valor_compu)

        if valor_lavadora == "":
            mueble_m12 = 0
            mueble_m12 = float(mueble_m12)
        else:
            mueble_m12 = float(valor_lavadora)

        if valor_secadora == "":
            mueble_m13 = 0
            mueble_m13 = float(mueble_m13)
        else:
            mueble_m13 = float(valor_secadora)

        bienes_muebles= mueble_m + mueble_m2 + mueble_m3 + mueble_m4 + mueble_m5 + mueble_m6 + mueble_m7 + mueble_m8 + mueble_m9 + mueble_m10 + mueble_m11 + mueble_m12 + mueble_m13

        if bienes_muebles >= 10001:
            bienes_muebles_n = 3
        elif bienes_muebles >= 5001 and bienes_muebles <= 10000:
            bienes_muebles_n = 2
        elif bienes_muebles >= 2001 and bienes_muebles <= 5000:
            bienes_muebles_n = 1
        elif bienes_muebles <= 2000:
            bienes_muebles_n = 0

        if aporte_liquido == "":
            ingresos_m = 0
            ingresos_m = float(ingresos_m)
        else:
            ingresos_m = float(aporte_liquido)
        
        if aporte_mama == "":
            ingresos_m2 = 0
            ingresos_m2 = float(ingresos_m2)
        else:
            ingresos_m2 = float(aporte_mama)
        
        if aporte_papa == "":
            ingresos_m3 = 0
            ingresos_m3 = float(ingresos_m3)
        else:
            ingresos_m3 = float(aporte_papa)
        
        if aporte_remesas == "":
            ingresos_m4 = 0
            ingresos_m4 = float(ingresos_m4)
        else:
            ingresos_m4 = float(aporte_remesas)
        
        if aporte_otros == "":
            ingresos_m5 = 0
            ingresos_m5 = float(ingresos_m5)
        else:
            ingresos_m5 = float(aporte_otros)
        
        ingresos_familia = ingresos_m + ingresos_m2 + ingresos_m3 + ingresos_m3 + ingresos_m4 + ingresos_m5

        if ingresos_familia >= 20000:
            ingresos_familiares_n = 4
        elif ingresos_familia >= 8001 and ingresos_familia <= 20000:
            ingresos_familiares_n = 3
        elif ingresos_familia >= 1501 and ingresos_familia <= 8000:
            ingresos_familiares_n = 2
        elif ingresos_familia >= 401 and ingresos_familia <= 1500:
            ingresos_familiares_n = 1
        elif ingresos_familia <= 400:
            ingresos_familiares_n = 0

        if cantidad_alimento == "":
            egresos_m = 0
            egresos_m = float(egresos_m)
        else:
            egresos_m = float(cantidad_alimento)
        
        if cantidad_pago_casa == "":
            egresos_m2 = 0
            egresos_m2 = float(egresos_m2)
        else:
            egresos_m2 = float(cantidad_pago_casa)
        
        if cantidad_abono_prestamo == "":
            egresos_m3 = 0
            egresos_m3= float(egresos_m3)
        else:
            egresos_m3= float(cantidad_abono_prestamo)

        if cantidad_abono_tarjetas == "":
            egresos_m4 = 0
            egresos_m4 = float(egresos_m4)
        else:
            egresos_m4 = float(cantidad_abono_tarjetas)

        if cantidad_serbasicos == "":
            egresos_m5 = 0
            egresos_m5 = float(egresos_m5)
        else:
            egresos_m5 = float(cantidad_serbasicos)

        if cantidad_educacion == "":
            egresos_m6 = 0
            egresos_m6 = float(egresos_m6)
        else:
            egresos_m6 = float(cantidad_educacion)

        if cantidad_transporte == "":
            egresos_m7 = 0
            egresos_m7 = float(egresos_m7)
        else:
            egresos_m7 = float(cantidad_transporte)

        if cantidad_combustible == "":
            egresos_m8 = 0
            egresos_m8 = float(egresos_m8)
        else:
            egresos_m8 = float(cantidad_combustible)

        if cantidad_ayuda_parientes == "":
            egresos_m9 = 0
            egresos_m9 = float(egresos_m9)
        else:
            egresos_m9 = float(cantidad_ayuda_parientes)

        if cantidad_salud == "":
            egresos_m10 = 0
            egresos_m10 = float(egresos_m10)
        else:
            egresos_m10 = float(cantidad_salud)

        if cantidad_internet == "":
            egresos_m11 = 0
            egresos_m11 = float(egresos_m11)
        else:
            egresos_m11= float(cantidad_internet)

        if cantidad_cable == "":
            egresos_m12 = 0
            egresos_m12 = float(egresos_m12)
        else:
            egresos_m12 = float(cantidad_cable)

        if cantidad_otros == "":
            egresos_m13 = 0
            egresos_m13 = float(egresos_m13)
        else:
            egresos_m13 = float(cantidad_otros)

        egresos_mensuales = egresos_m + egresos_m2 + egresos_m3 + egresos_m4 + egresos_m5 + egresos_m6 + egresos_m7 + egresos_m8 + egresos_m9 + egresos_m10 + egresos_m11 + egresos_m12 + egresos_m13

        if egresos_mensuales >= 10000:
            egresos_familiares_n = 4
        elif egresos_mensuales >= 5001 and egresos_mensuales <= 10000:
            egresos_familiares_n = 3
        elif egresos_mensuales >= 1501 and egresos_mensuales <= 5000:
            egresos_familiares_n = 2
        elif egresos_mensuales >= 401 and egresos_mensuales <= 1500:
            egresos_familiares_n = 1
        elif egresos_mensuales <= 400:
            egresos_familiares_n = 0


        Carrera(nombre_carrera=nombre_carrera).save()

        Estudiantes(nombre_estudiante=nombre_estudiante, vive_en=vive_en, vive_con=vive_con, estado_civil=estado_civil, lugar_nacimiento=lugar_nacimiento, fecha_nacimiento=fecha_nacimiento,
        edad_estudiante=edad_estudiante,primer_apellido=primer_apellido, segundo_apellido=segundo_apellido,
        beca_escuela=beca_escuela, tipo_titulo=tipo_titulo, usuario_id=usuario_id, tipo_ingreso=tipo_ingreso, bachiller_opcion=bachiller_opcion, bachiller_opcion2=bachiller_opcion2, beca_precio=beca_precio, ciclo_estudiado=ciclo_estudiado,
        ciclo_estudiado2=ciclo_estudiado2, cuota_pagaba=cuota_pagaba, cuota_pagaba2=cuota_pagaba2, lugar_procedencia=lugar_procedencia, lugar_procedencia2=lugar_procedencia2, pago_cuota=pago_cuota, pago_cuota2=pago_cuota2, estado='1').save()

        Contacto_Estudiante(direccion_exacta=direccion_exacta, telefono_fijo=telefono_fijo, celular=celular, email=email, usuario_id=usuario_id).save()

        Grupo_familiare(cantidad_familiares=cantidad_familiares, edad_familiar=edad_familiar, usuario_id=usuario_id, edad_familiar10=edad_familiar10, edad_familiar2=edad_familiar2, 
        edad_familiar3=edad_familiar3, edad_familiar4=edad_familiar4, edad_familiar5=edad_familiar5, edad_familiar6=edad_familiar6, edad_familiar7=edad_familiar7, edad_familiar8=edad_familiar8, edad_familiar9=edad_familiar9,
        lugar_trabajo=lugar_trabajo, lugar_trabajo10=lugar_trabajo10, lugar_trabajo2=lugar_trabajo2, lugar_trabajo3=lugar_trabajo3, lugar_trabajo4=lugar_trabajo4, lugar_trabajo5=lugar_trabajo5, lugar_trabajo6=lugar_trabajo6,
        lugar_trabajo7=lugar_trabajo7, lugar_trabajo8=lugar_trabajo8, lugar_trabajo9=lugar_trabajo9, nombre=nombre, nombre10=nombre10, nombre2=nombre2, nombre3=nombre3, nombre4=nombre4, nombre5=nombre5, nombre6=nombre6,
        nombre7=nombre7, nombre8=nombre8, nombre9=nombre9, parentesco=parentesco, parentesco10=parentesco10, parentesco2=parentesco2, parentesco3=parentesco3, parentesco4=parentesco4, parentesco5=parentesco5, parentesco6=parentesco6,
        parentesco7=parentesco7, parentesco8=parentesco8, parentesco9=parentesco9, profesion=profesion, profesion10=profesion10, profesion2=profesion2, profesion3=profesion3, profesion4=profesion4, profesion5=profesion5,
        profesion6=profesion6, profesion7=profesion7, profesion8=profesion8, profesion9=profesion9).save()

        Educacion_Familia(nombre_familiar=nombre_familiar, nombre_familiar2=nombre_familiar2, nombre_familiar3=nombre_familiar3, grado_educacion=grado_educacion, grado_educacion2=grado_educacion2, grado_educacion3=grado_educacion3,
        centro_estudios=centro_estudios, centro_estudios2=centro_estudios2, centro_estudios3=centro_estudios3, cuota=cuota, cuota2=cuota2, cuota3=cuota3, responsable_cuota=responsable_cuota, responsable_cuota2=responsable_cuota2,
        responsable_cuota3=responsable_cuota3, usuario_id=usuario_id).save()

        Bienes_Familiare(propiedad_familia=propiedad_familia, propiedad_familia2=propiedad_familia2, propiedad_familia3=propiedad_familia3, direccion_propiedad=direccion_propiedad, direccion_propiedad2=direccion_propiedad2,
        direccion_propiedad3=direccion_propiedad3, n_habitaciones=n_habitaciones, n_habitaciones2=n_habitaciones2, n_habitaciones3=n_habitaciones3, n_baños=n_baños, n_baños2=n_baños2, n_baños3=n_baños3, inst_vendedora=inst_vendedora,
        inst_vendedora2=inst_vendedora2, inst_vendedora3=inst_vendedora3, cuota_mensual=cuota_mensual, cuota_mensual2=cuota_mensual2, cuota_mensual3=cuota_mensual3, valor_actual=valor_actual, valor_actual2=valor_actual2, valor_actual3=valor_actual3,
        posee_vehiculo=posee_vehiculo, tipo_vehiculo=tipo_vehiculo, tipo_vehiculo2=tipo_vehiculo2, marca_vehiculo=marca_vehiculo, marca_vehiculo2=marca_vehiculo2, año_vehiculo=año_vehiculo, año_vehiculo2=año_vehiculo2,
        valor_vehiculo=valor_vehiculo, valor_vehiculo2=valor_vehiculo2, cantidad_mueble_comedor=cantidad_mueble_comedor, valor_mueble_comedor=valor_mueble_comedor, cantidad_refri=cantidad_refri, valor_refri=valor_refri,
        cantidad_cocina=cantidad_cocina, valor_cocina=valor_cocina, cantidad_horno=cantidad_horno, valor_horno=valor_horno, cantidad_licuadora=cantidad_licuadora, valor_licuadora=valor_licuadora, cantidad_tv=cantidad_tv,
        valor_tv=valor_tv, cantidad_teatro=cantidad_teatro, valor_teatro=valor_teatro, cantidad_sonido=cantidad_sonido, valor_sonido=valor_sonido, cantidad_camara=cantidad_camara, valor_camara=valor_camara, cantidad_compu=cantidad_compu,
        valor_compu=valor_compu, cantidad_lavadora=cantidad_lavadora, valor_lavadora=valor_lavadora, cantidad_secadora=cantidad_secadora, valor_secadora=valor_secadora, usuario_id=usuario_id).save()

        datos_economicos_familia(trabajo_alumno=trabajo_alumno, salario_alumno=salario_alumno, descuento_alumno=descuento_alumno, aporte_liquido=aporte_liquido, trabajo_mama=trabajo_mama, salario_mama=salario_mama, descuento_mama=descuento_mama,
        aporte_mama=aporte_mama, trabajo_papa=trabajo_papa, salario_papa=salario_papa, descuento_papa=descuento_papa, aporte_papa=aporte_papa, trabajo_remesas=trabajo_remesas, salario_remesas=salario_remesas, descuento_remesas=descuento_remesas,
        aporte_remesas=aporte_remesas, trabajo_otros=trabajo_otros, salario_otros=salario_otros, descuento_otros=descuento_otros, aporte_otros=aporte_otros, cantidad_alimento=cantidad_alimento, detalles_alimento=detalles_alimento,
        cantidad_pago_casa=cantidad_pago_casa, detalles_pago_casa=detalles_pago_casa, cantidad_abono_prestamo=cantidad_abono_prestamo, detalles_abono_prestamo=detalles_abono_prestamo, cantidad_abono_tarjetas=cantidad_abono_tarjetas,
        detalles_abono_tarjetas=detalles_abono_tarjetas, cantidad_serbasicos=cantidad_serbasicos, detalles_serbasicos=detalles_serbasicos, cantidad_educacion=cantidad_educacion, detalles_educacion=detalles_educacion,
        cantidad_transporte=cantidad_transporte, detalles_transporte=detalles_transporte ,cantidad_combustible=cantidad_combustible, detalles_combustible=detalles_combustible ,cantidad_ayuda_parientes=cantidad_ayuda_parientes, detalles_ayuda_parientes=detalles_ayuda_parientes,
        cantidad_salud=cantidad_salud, detalles_salud=detalles_salud, cantidad_internet=cantidad_internet, detalles_internet=detalles_internet, cantidad_cable=cantidad_cable, detalles_cable=detalles_cable, cantidad_otros=cantidad_otros,
        detalles_otros=detalles_otros, usuario_id=usuario_id).save()

        Referencia(nombre_amigo=nombre_amigo, carrera_amigo=carrera_amigo, medio_referencia=medio_referencia, usuario_id=usuario_id).save()

        Declaracion(nombre_aspirante=nombre_aspirante, firma_aspirante=firma_aspirante, nombre_responsable=nombre_responsable, firma_responsable=firma_responsable, usuario_id=usuario_id, fecha_firmo=fecha_firmo).save()

        datos_neurona(vive_en_n=vive_en_n, vive_con_n=vive_con_n, estado_civil_n=estado_civil_n, cuota_institucion_n=cuota_institucion_n, beca_n=beca_n, miembros_fam_n=miembros_fam_n, egresos_n=egresos_n, 
        propiedades_n=propiedades_n, vehiculo_n=vehiculo_n, bienes_muebles_n=bienes_muebles_n, ingresos_familiares_n=ingresos_familiares_n, egresos_familiares_n=egresos_familiares_n, usuario_id=usuario_id).save()

        messages.success(request, 'Registro añadido')
        return HttpResponseRedirect(reverse('index'))


def prueba_estudio(request):
    canvas=request.POST['canvas']

    canvas2=request.POST['canvas2']
  
    return render(request, "prueba_estudio.html", {"canvas":canvas, "canvas2":canvas2})

def ver_cuota(request):
    page = "estudio"
    groups = Group.objects.values_list().filter(user=request.user)[0][1]
    user= request.user
    id= user.id
    estudiante = Estudiantes.objects.values().filter(usuario_id=id)
    resultado_cuota= datos_neurona.objects.values().filter(usuario_id=id)
    return render(request, "ver_cuota.html", {"page":page, "groups":groups, "resultado_cuota":resultado_cuota, "estudiante":estudiante})


def calcular_cuota(request):
    user= request.user
    usuario_id= user.id

    neurona= datos_neurona.objects.values_list('vive_en_n', 'vive_con_n', 'estado_civil_n', 'cuota_institucion_n', 'beca_n',
    'miembros_fam_n', 'egresos_n', 'propiedades_n', 'vehiculo_n', 'bienes_muebles_n', 'ingresos_familiares_n', 'egresos_familiares_n').filter(usuario_id=usuario_id)[0]
    df=pd.read_csv(('EstudioSocioeconomico/estudiosocioeconomico.csv'))
    #print(df.head())
    x= df.drop(columns=['cuota_asignada'])
    y= df[['cuota_asignada']]
    model= keras.models.Sequential()
    model.add(keras.layers.Dense(25, activation='relu', input_shape=(12,)))
    model.add(keras.layers.Dense(25, activation='relu'))
    model.add(keras.layers.Dense(25, activation='relu'))
    model.add(keras.layers.Dense(25, activation='relu'))
    model.add(keras.layers.Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x, y, epochs=100, callbacks=[keras.callbacks.EarlyStopping(patience=5)])

    test_data=np.array(list(neurona))
    final_data=model.predict(test_data.reshape(1,12), batch_size=1)
    cuota_estudiante=math.ceil(final_data)

    cuota = datos_neurona.objects.get(usuario_id=usuario_id)
    cuota.cuota_estudiante = cuota_estudiante
    cuota.save()

    estudiante=Estudiantes.objects.get(usuario_id=usuario_id)
    estudiante.estado = "2"
    estudiante.save()

    

    return HttpResponseRedirect(reverse('ver_cuota'))

def prueba(request):
    imagen = request.POST('imagen')
    return render(request, 'prueba.html', {"imagen":imagen})