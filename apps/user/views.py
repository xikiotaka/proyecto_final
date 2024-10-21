from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Función para renderizar la página de registro
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirigir a la página de inicio de sesión
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado con éxito, felicidades!')
            return redirect('profile')  # Redirigir a la página de perfil
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def user(request):
    return render(request, 'user.html')
