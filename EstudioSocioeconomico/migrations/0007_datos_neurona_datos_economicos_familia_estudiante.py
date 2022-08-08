# Generated by Django 4.0.3 on 2022-07-17 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EstudioSocioeconomico', '0006_datos_economicos_familia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='datos_neurona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vive_en_n', models.IntegerField()),
                ('vive_con_n', models.IntegerField()),
                ('estado_civil_n', models.IntegerField()),
                ('cuota_institucion_n', models.IntegerField()),
                ('beca_n', models.IntegerField()),
                ('miembros_fam_n', models.IntegerField()),
                ('egresos_n', models.IntegerField()),
                ('propiedades_n', models.IntegerField()),
                ('vehiculo_n', models.IntegerField()),
                ('bienes_muebles_n', models.IntegerField()),
                ('ingresos_familiares_n', models.IntegerField()),
                ('egresos_familiares_n', models.IntegerField()),
                ('puntuacion', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='datos_economicos_familia',
            name='estudiante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EstudioSocioeconomico.estudiantes'),
        ),
    ]