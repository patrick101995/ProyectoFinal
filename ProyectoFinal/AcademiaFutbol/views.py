
from dataclasses import field
from msilib.schema import Class
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
from AcademiaFutbol.forms import ContactoFormulario


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

def contactoFormulario(request):
    
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)

        if miFormulario.is_valid:
            #informacion = miFormulario.cleaned_data
            informacion = miFormulario
            comentario = FormularioContacto (pNombre=informacion['Nombre'], sNombre=informacion['Apellido'], correo=informacion['correo'],telefono=informacion['telefono'],comentarios=informacion['comentarios'])

            comentario.save

            return render(request, "AcademiaFutbol/inicio.html")

    else:
        miFormulario = ContactoFormulario()

    return render(request, "AcademiaFutbol/contacto.html", {"miFormulario":miFormulario})

#def contactoFormulario(request):
    
#    if request.method == 'POST':
#        datos = FormularioContacto(request.POST['Nombre'], request.POST['Apellido'],request.POST['correo'], request.POST['telefono'], request.POST['comentarios'])

#        datos.save()

#        return render(request, "AcademiaFutbol/inicio.html")

#    return render(request, "AcademiaFutbol/contacto.html")

class ContactoList(ListView):
    model = FormularioContacto
    template_name = "AcademiaFutbol/contacto.html"