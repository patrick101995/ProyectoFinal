
from unicodedata import name
from django.urls import path, include
from AcademiaFutbol import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('altaJugador', views.altaJugador, name="AltaJugador"),
    path('altaGrupo', views.altaGrupo, name="AltaGrupo"),
    path('buscar', views.buscar),
    path('formulario_jugador', views.registro_jugador, name="formulario_jugador"),
    path('formulario_grupo', views.registro_grupo, name="formulario_grupo")
]
