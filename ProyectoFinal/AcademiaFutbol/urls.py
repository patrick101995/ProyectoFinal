
from unicodedata import name
from django.urls import path, include
from AcademiaFutbol import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
]
