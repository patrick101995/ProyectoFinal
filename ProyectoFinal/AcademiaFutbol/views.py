
from dataclasses import field
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AcademiaFutbol.models import Jugador, Grupo, FormularioContacto
from django.urls import reverse_lazy


# Create your views here.


def inicio(request):
    return render(request, "AcademiaFutbol/inicio.html")

class GrupoList (ListView):
    model = Grupo
    template_name = "AcademiaFutbol/grupos.html"
    

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

class Contacto(CreateView):
    model: FormularioContacto

    field = ['Primer Nombre', 'Segundo Nombre', 'Email','Telefono', 'Comentario']
    template_name = 'AcademiaFutbol/contacto.html'
