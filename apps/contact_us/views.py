from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacto
from .forms import ContactoForm 
from django.shortcuts import render 

def contact_us(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contact_us')  ###Para poder redirigir a la página de contacto, ver cómo hacerlo en HTML
    else:
        form = ContactoForm()
    return render(request, 'contact_us.html', {'form': form})

def list_contacts(request):
    contactos = Contacto.objects.all()  ###Para poder obtener todos los contacos, hay que ver si vamos a necesitar que se contemplen todos o no
    return render(request, 'list_contacts.html', {'contactos': contactos})

def contact_us(request):
    return render(request, 'contact_us.html')


    