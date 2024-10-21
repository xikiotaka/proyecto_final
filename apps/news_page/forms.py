from django import forms
from django.utils.html import strip_tags  
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpo', 'calificacion']

    def clean_cuerpo(self):
        cuerpo = self.cleaned_data.get('cuerpo')
        cuerpo = strip_tags(cuerpo) 
        if not cuerpo:
            raise forms.ValidationError("El cuerpo del comentario no puede estar vacío.")
        return cuerpo
