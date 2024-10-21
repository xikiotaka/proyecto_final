from django.urls import path
from apps.landing_page import views

urlpatterns = [
    ###Ruta para la landing page como raíz
    path('', views.landing_page, name='landing_page'),  ###URL raíz

    ###Rutas para la landing_page
    path('landing_pages/', views.landing_page_lista, name='landing_page_list'),
    path('landing_pages/<int:pk>/', views.landing_page_detalles, name='landing_page_detail'),

    ###Rutas para las noticias
    path('noticias/', views.noticia_lista, name='noticia_list'),
    path('noticias/<int:pk>/', views.noticia_detalles, name='noticia_detail'),
    path('noticias/nueva/', views.crear_noticias, name='crear_noticia'),
    path('noticias/<int:pk>/editar/', views.editar_noticias, name='editar_noticia'),
]
