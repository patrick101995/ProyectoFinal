from django import forms

class ContactoFormulario(forms.Form):

    Nombre = forms.CharField()
    Apellido = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.IntegerField()
    comentarios = forms.CharField()