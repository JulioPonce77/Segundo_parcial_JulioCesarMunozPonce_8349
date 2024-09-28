from django import forms
from .models import Profesor, Mascota

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombres', 'apellido', 'genero']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'genero', 'profesor']
