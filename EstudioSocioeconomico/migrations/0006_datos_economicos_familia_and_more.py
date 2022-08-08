# Generated by Django 4.0.3 on 2022-07-16 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EstudioSocioeconomico', '0005_remove_carrera_id_carreras_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='datos_economicos_familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajo_alumno', models.CharField(max_length=75)),
                ('salario_alumno', models.IntegerField()),
                ('descuento_alumno', models.IntegerField()),
                ('aporte_liquido', models.IntegerField()),
                ('trabajo_mama', models.CharField(max_length=75)),
                ('salario_mama', models.IntegerField()),
                ('descuento_mama', models.IntegerField()),
                ('aporte_mama', models.IntegerField()),
                ('trabajo_papa', models.CharField(max_length=75)),
                ('salario_papa', models.IntegerField()),
                ('descuento_papa', models.IntegerField()),
                ('aporte_papa', models.IntegerField()),
                ('trabajo_remesas', models.CharField(max_length=75)),
                ('salario_remesas', models.IntegerField()),
                ('descuento_remesas', models.IntegerField()),
                ('aporte_remesas', models.IntegerField()),
                ('trabajo_otros', models.CharField(max_length=75)),
                ('salario_otros', models.IntegerField()),
                ('descuento_otros', models.IntegerField()),
                ('aporte_otros', models.IntegerField()),
                ('cantidad_alimento', models.IntegerField()),
                ('detalles_alimento', models.CharField(max_length=150)),
                ('cantidad_pago_casa', models.IntegerField()),
                ('detalles_pago_casa', models.CharField(max_length=150)),
                ('cantidad_abono_prestamo', models.IntegerField()),
                ('detalles_abono_prestamo', models.CharField(max_length=150)),
                ('cantidad_abono_tarjetas', models.IntegerField()),
                ('detalles_abono_tarjetas', models.CharField(max_length=150)),
                ('cantidad_serbasicos', models.IntegerField()),
                ('detalles_serbasicos', models.CharField(max_length=150)),
                ('cantidad_educacion', models.IntegerField()),
                ('detalles_educacion', models.CharField(max_length=150)),
                ('cantidad_transporte', models.IntegerField()),
                ('detalles_transporte', models.CharField(max_length=150)),
                ('cantidad_combustible', models.IntegerField()),
                ('detalles_combustible', models.CharField(max_length=150)),
                ('cantidad_ayuda_parientes', models.IntegerField()),
                ('detalles_ayuda_parientes', models.CharField(max_length=150)),
                ('cantidad_salud', models.IntegerField()),
                ('detalles_salud', models.CharField(max_length=150)),
                ('cantidad_internet', models.IntegerField()),
                ('detalles_internet', models.CharField(max_length=150)),
                ('cantidad_cable', models.IntegerField()),
                ('detalles_cable', models.CharField(max_length=150)),
                ('cantidad_otros', models.IntegerField()),
                ('detalles_otros', models.CharField(max_length=150)),
                ('observaciones', models.CharField(max_length=140)),
            ],
        ),
        migrations.RemoveField(
            model_name='grupo_familiare',
            name='detalles_egresos_familiares',
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='tipo_titulo',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar10',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar3',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar4',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar5',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar6',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar7',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar8',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='edad_familiar9',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo10',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo2',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo3',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo4',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo5',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo6',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo7',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo8',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='lugar_trabajo9',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre10',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre2',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre3',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre4',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre5',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre6',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre7',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre8',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='nombre9',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco10',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco2',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco3',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco4',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco5',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco6',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco7',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco8',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='parentesco9',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion10',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion2',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion3',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion4',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion5',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion6',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion7',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion8',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo_familiare',
            name='profesion9',
            field=models.CharField(default=0, max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrera',
            name='facultad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.facultad'),
        ),
        migrations.AlterField(
            model_name='contacto_estudiante',
            name='estudiante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes'),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.carrera'),
        ),
        migrations.AlterField(
            model_name='grupo_familiare',
            name='estudiante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes'),
        ),
        migrations.AlterField(
            model_name='propiedades',
            name='estudiante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes'),
        ),
        migrations.AlterField(
            model_name='recibos',
            name='estudiante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes'),
        ),
        migrations.AlterField(
            model_name='referencia',
            name='estudiante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes'),
        ),
        migrations.CreateModel(
            name='Educacion_Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_familiar', models.CharField(max_length=75)),
                ('nombre_familiar2', models.CharField(max_length=75)),
                ('nombre_familiar3', models.CharField(max_length=75)),
                ('grado_educacion', models.CharField(max_length=75)),
                ('grado_educacion2', models.CharField(max_length=75)),
                ('grado_educacion3', models.CharField(max_length=75)),
                ('centro_estudios', models.CharField(max_length=75)),
                ('centro_estudios2', models.CharField(max_length=75)),
                ('centro_estudios3', models.CharField(max_length=75)),
                ('cuota', models.IntegerField()),
                ('cuota2', models.IntegerField()),
                ('cuota3', models.IntegerField()),
                ('responsable_cuota', models.CharField(max_length=50)),
                ('responsable_cuota2', models.CharField(max_length=50)),
                ('responsable_cuota3', models.CharField(max_length=50)),
                ('estudiante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes')),
            ],
        ),
        migrations.CreateModel(
            name='Bienes_Familiare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propiedad_familia', models.CharField(max_length=30)),
                ('propiedad_familia2', models.CharField(max_length=30)),
                ('propiedad_familia3', models.CharField(max_length=30)),
                ('direccion_propiedad', models.CharField(max_length=150)),
                ('direccion_propiedad2', models.CharField(max_length=150)),
                ('direccion_propiedad3', models.CharField(max_length=150)),
                ('n_habitaciones', models.IntegerField()),
                ('n_habitaciones2', models.IntegerField()),
                ('n_habitaciones3', models.IntegerField()),
                ('n_baños', models.IntegerField()),
                ('n_baños2', models.IntegerField()),
                ('n_baños3', models.IntegerField()),
                ('inst_vendedora', models.CharField(max_length=100)),
                ('inst_vendedora2', models.CharField(max_length=100)),
                ('inst_vendedora3', models.CharField(max_length=100)),
                ('cuota_mensual', models.IntegerField()),
                ('cuota_mensual2', models.IntegerField()),
                ('cuota_mensual3', models.IntegerField()),
                ('valor_actual', models.IntegerField()),
                ('valor_actual2', models.IntegerField()),
                ('valor_actual3', models.IntegerField()),
                ('posee_vehiculo', models.CharField(max_length=3)),
                ('tipo_vehiculo', models.CharField(max_length=50)),
                ('tipo_vehiculo2', models.CharField(max_length=50)),
                ('marca_vehiculo', models.CharField(max_length=50)),
                ('marca_vehiculo2', models.CharField(max_length=50)),
                ('año_vehiculo', models.CharField(max_length=50)),
                ('año_vehiculo2', models.CharField(max_length=50)),
                ('valor_vehiculo', models.IntegerField()),
                ('valor_vehiculo2', models.IntegerField()),
                ('cantidad_mueble_sala', models.IntegerField()),
                ('valor_mueble_sala', models.IntegerField()),
                ('cantidad_mueble_comedor', models.IntegerField()),
                ('valor_mueble_comedor', models.IntegerField()),
                ('cantidad_refri', models.IntegerField()),
                ('valor_refri', models.IntegerField()),
                ('cantidad_cocina', models.IntegerField()),
                ('valor_cocina', models.IntegerField()),
                ('cantidad_horno', models.IntegerField()),
                ('valor_horno', models.IntegerField()),
                ('cantidad_licuadora', models.IntegerField()),
                ('valor_licuadora', models.IntegerField()),
                ('cantidad_tv', models.IntegerField()),
                ('valor_tv', models.IntegerField()),
                ('cantidad_teatro', models.IntegerField()),
                ('valor_teatro', models.IntegerField()),
                ('cantidad_sonido', models.IntegerField()),
                ('valor_sonido', models.IntegerField()),
                ('cantidad_camara', models.IntegerField()),
                ('valor_camara', models.IntegerField()),
                ('cantidad_compu', models.IntegerField()),
                ('valor_compu', models.IntegerField()),
                ('cantidad_lavadora', models.IntegerField()),
                ('valor_lavadora', models.IntegerField()),
                ('cantidad_secadora', models.IntegerField()),
                ('valor_secadora', models.IntegerField()),
                ('estudiante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes')),
            ],
        ),
    ]