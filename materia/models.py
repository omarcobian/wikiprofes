from django.db import models
from profesor.models import Profesor
from django.contrib.auth.models import User

# Create your models here.
class Materia(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    departamento = models.CharField(max_length=50)
    profesores = models.ManyToManyField(Profesor, through='publicacion.Publicacion')#Indica relacion de muchos a muchos
    usuarios = models.ManyToManyField(User, through='publicacion.Publicacion')

    def __str__(self):
        return f'{self.clave} {self.nombre}'