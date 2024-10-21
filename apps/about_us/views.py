from django.shortcuts import render, get_object_or_404, redirect
from .models import AboutUs
from .forms import AboutUsForm
from django.shortcuts import render


def about_us_lista(request):
    about_us = AboutUs.objects.all()
    return render(request, 'about_us_list.html', {'about_us': about_us})

def about_us_detalle(request, pk):
    about_us = get_object_or_404(AboutUs, pk=pk)
    return render(request, 'about_us_detail.html', {'about_us': about_us})

def crear_about_us(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_us_list')
    else:
        form = AboutUsForm()
    return render(request, 'crear_about_us.html', {'form': form})

def editar_about_us(request, pk):
    about_us = get_object_or_404(AboutUs, pk=pk)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect('about_us_detail', pk=about_us.pk)
    else:
        form = AboutUsForm(instance=about_us)
    return render(request, 'editar_about_us.html', {'form': form, 'about_us': about_us})

def about_us(request):
    return render(request, 'about_us.html')