from django.urls import path
from apps.contact_us import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),  ###Cambié a '' para manejar /contact_us/
    path('list_contacts/', views.list_contacts, name='list_contacts'),
]
