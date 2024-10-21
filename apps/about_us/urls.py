from django.urls import path
from apps.about_us import views

urlpatterns = [
    path('', views.about_us, name='about_us'),  
    path('list/', views.about_us_lista, name='about_us_list'),  
    path('<int:pk>/', views.about_us_detalle, name='about_us_detail'),  
    path('nuevo/', views.crear_about_us, name='crear_about_us'),  
    path('<int:pk>/editar/', views.editar_about_us, name='editar_about_us'),  
    path('info/', views.about_us, name='about_us_info'),
]
