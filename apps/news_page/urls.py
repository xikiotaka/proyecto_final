from django.urls import path
from apps.news_page import views

urlpatterns = [
    ### Rutas para publicaciones
    path('posts/', views.post_list, name='post_list'),  ### Publicaciones
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),  

    ### Ruta para crear una nueva publicación
    path('posts/nuevo/', views.PostCreateView.as_view(), name='post_create'),

    ### Ruta para agregar un "me gusta" a una publicación
    path('posts/<int:post_id>/like/', views.add_like, name='add_like'),

    ### Ruta para la lista de categorías
    path('categorias/', views.categoria_list, name='categoria_list'),

    ### Ruta para una respuesta simple de prueba
    path('example/', views.example_response, name='example_response'),

    ### Ruta para la página de noticias
    path('', views.news_page, name='news_page'),  # Cambiado a '' para manejar /news_page/
]
