
from pyexpat import model
from django.db import models

# Create your models here.

class Grupo (models.Model):
    categoria = models.CharField(max_length=30)
    edadMinima = models.IntegerField()
    edadMazima = models.IntegerField()

class Jugador (models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    estatura = models.IntegerField()
    