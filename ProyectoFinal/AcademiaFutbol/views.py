
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AcademiaFutbol.models import Jugador, Grupo


# Create your views here.


def inicio(request):
    return render(request, "AcademiaFutbol/inicio.html")

class GrupoList (ListView):
    model = Grupo
    template_name = "AcademiaFutbol/grupos.html"

class RegistroJugadorList(ListView):
    model = Jugador
    template_name = "AcademiaFutbol/registroJugador.html"