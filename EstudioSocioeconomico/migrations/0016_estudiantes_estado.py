# Generated by Django 4.0.3 on 2022-07-19 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EstudioSocioeconomico', '0015_carrera_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='estado',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
