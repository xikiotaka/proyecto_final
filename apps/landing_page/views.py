from django.shortcuts import render, get_object_or_404, redirect
from .models import LandingPage, Noticia
from .forms import NoticiaForm
from django.shortcuts import render

def landing_page_lista(request):
    landing_pages = LandingPage.objects.all()
    return render(request, 'landing_page_list.html', {'landing_pages': landing_pages})

def landing_page_detalles(request, pk):
    landing_page = get_object_or_404(LandingPage, pk=pk)
    return render(request, 'landing_page_detail.html', {'landing_page': landing_page})

def noticia_lista(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticia_list.html', {'noticias': noticias})

def noticia_detalles(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticia_detail.html', {'noticia': noticia})

def crear_noticias(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticia_list')
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form})

def editar_noticias(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticia_detail', pk=noticia.pk)
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'editar_noticia.html', {'form': form, 'noticia': noticia})

def landing_page(request):
    return render(request, 'landing_page.html')