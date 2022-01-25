from django import forms

class Registro_jugador(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    estatura = forms.IntegerField()
    
class Registro_grupo(forms.Form):
    categoria = forms.CharField()
    edadMinima = forms.IntegerField()
    edadMazima = forms.IntegerField()