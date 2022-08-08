from django.contrib import admin

from EstudioSocioeconomico.models import Usuario, Facultad, Carrera, Estudiantes, Contacto_Estudiante, Propiedades, Grupo_familiare, Referencia, Recibos

# Register your models here.

admin.site.register(Usuario)

admin.site.register(Facultad)

admin.site.register(Carrera)

admin.site.register(Estudiantes)

admin.site.register(Contacto_Estudiante)

admin.site.register(Propiedades)

admin.site.register(Grupo_familiare)

admin.site.register(Referencia)

admin.site.register(Recibos)
