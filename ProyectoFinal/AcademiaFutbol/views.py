
from django.http import HttpResponse
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
    categorias = Grupo.objects.all
    

class RegistroJugadorList(ListView):
    model = Jugador
    template_name = "AcademiaFutbol/registroJugador.html"


def buscar(request):
    
    #respuesta = f"Estoy buscando el grupo: {request.GET['grupo']}"

    if request.GET["categoria"]:
        categoria = request.GET['categoria']
        categoria = Grupo.objects.filter(categoria__icontains=categoria)

        return render(request, "AcademiaFutbol/resultadoBusqueda.html", {"categoria":categoria})
    
    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)