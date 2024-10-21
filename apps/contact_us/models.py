from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=100, verbose_name="Nombre y Apellido")
    email = models.EmailField(validators=[EmailValidator()], verbose_name="Correo Electrónico")
    asunto = models.CharField(max_length=150, verbose_name="Asunto")  ###Aumenté un poco el length por las dudas
    fecha = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Fecha y Hora") 
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-fecha']  ###Organicé de forma ascendente para poder tener un orden

    def __str__(self):
        return f"{self.nombre_apellido} - {self.asunto}"  

