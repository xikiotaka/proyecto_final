from django.urls import path
from .views import vista_busqueda

urlpatterns = [
    path('', vista_busqueda, name='busqueda'),
]
