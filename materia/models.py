from django.db import models

# Create your models here.
class Materia(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    departamento = models.CharField(max_length=50)