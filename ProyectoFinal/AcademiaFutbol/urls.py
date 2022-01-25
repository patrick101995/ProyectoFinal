
from unicodedata import name
from django.urls import path, include
from AcademiaFutbol import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('grupos', views.GrupoList.as_view(), name="GrupoList"),
    path('registroJugador', views.RegistroJugadorList.as_view(), name="RegistroJugadorList"),
    path('buscar', views.buscar),
    path('contactoForm',views.contactoFormulario, name="contacto"),
    path('contacto', views.ContactoList.as_view(), name="ContactoList")
    
]
