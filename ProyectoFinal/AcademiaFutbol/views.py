
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from AcademiaFutbol.models import Jugador, Grupo, FormularioContacto
from AcademiaFutbol.forms import Registro_jugador, Registro_grupo, ContactoFormulario


# Create your views here.


def inicio(request):
    return render(request, "AcademiaFutbol/inicio.html")

class GrupoList (ListView):
    model = Grupo
    template_name = "AcademiaFutbol/grupos.html"
    categorias = Grupo.objects.all
    

# class RegistroJugadorList(ListView):
#     model = Jugador
#     template_name = "AcademiaFutbol/registroJugador.html"

def altaJugador(request):
    return render(request, 'AcademiaFutbol/altaJugador.html',
        {'jugadores': Jugador.objects.all()})
    
def altaGrupo(request):
    return render(request, 'AcademiaFutbol/altaGrupo.html',
        {'grupos': Grupo.objects.all()})


def buscar(request):
    
    #respuesta = f"Estoy buscando el grupo: {request.GET['grupo']}"

    if request.GET["categoria"]:
        categoria = request.GET['categoria']
        categoria = Grupo.objects.filter(categoria__icontains=categoria)

        return render(request, "AcademiaFutbol/resultadoBusqueda.html", {"categoria":categoria})
    
    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def registro_jugador(request):
    
    if request.method == "POST":
        formulario = Registro_jugador(request.POST)
    
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            Jugador.objects.create(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"], estatura=info["estatura"])
            
            return redirect("AltaJugador")
        
    else:
            
        formulario = Registro_jugador()
            
    return render(request, "AcademiaFutbol/formulario_jugador.html", {"formulario":formulario})

def registro_grupo(request):
    
    if request.method == "POST":
        formulario = Registro_grupo(request.POST)
    
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            Grupo.objects.create(categoria=info['categoria'], edadMinima=info['edadMinima'], edadMazima=info['edadMazima'])
            
            return redirect("AltaGrupo")
        
    else:
            
        formulario = Registro_grupo()
            
    return render(request, "AcademiaFutbol/formulario_grupo.html", {"formulario":formulario})


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
        
class ContactoList(ListView):
    model = FormularioContacto
    template_name = "AcademiaFutbol/contacto.html"