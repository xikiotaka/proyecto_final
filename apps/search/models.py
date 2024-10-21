from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
