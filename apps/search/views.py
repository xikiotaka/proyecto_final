from django.shortcuts import render
from .models import Articulo

def vista_busqueda(request):
    query = request.GET.get('q')
    if query:
        articulos = Articulo.objects.filter(titulo__icontains=query)
    else:
        articulos = Articulo.objects.all()
    return render(request, 'search.html', {'articulos': articulos, 'query': query})
