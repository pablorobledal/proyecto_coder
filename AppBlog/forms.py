from django import forms
from . import models

class CrearPosteo(forms.ModelForm):
    class Meta:
        model = models.Posteo
        fields = ['titulo', 'universo', 'cuerpo', 'imagen']