from django import forms
from .models import LandingPage, Noticia

class LandingPageForm(forms.ModelForm):
    class Meta:
        model = LandingPage
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen_destacada']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'subtitulo', 'contenido', 'categoria', 'imagen', 'activo']
