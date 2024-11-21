# Generated by Django 5.1.3 on 2024-11-20 03:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0001_initial'),
        ('profesor', '0001_initial'),
        ('publicacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='profesores',
            field=models.ManyToManyField(through='publicacion.Publicacion', to='profesor.profesor'),
        ),
        migrations.AddField(
            model_name='materia',
            name='usuarios',
            field=models.ManyToManyField(through='publicacion.Publicacion', to=settings.AUTH_USER_MODEL),
        ),
    ]