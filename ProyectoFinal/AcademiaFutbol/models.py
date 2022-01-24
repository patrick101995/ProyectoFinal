
from msilib.schema import Class
from pyexpat import model
from django.db import models

# Create your models here.

class Grupo (models.Model):
    categoria = models.CharField(max_length=30)
    edadMinima = models.IntegerField()
    edadMazima = models.IntegerField()

    def __str__(self):
        return self.categoria

class Jugador (models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    estatura = models.IntegerField()

class FormularioContacto (models.Model):
    Pnombre = models.CharField(max_length=40)
    Snombre = models.CharField(max_length=40)
    correo = models.EmailField()
    telefono = models.IntegerField()
    comentarios = models.CharField(max_length=100)

    def __str__(self):
        return self.Pnombre