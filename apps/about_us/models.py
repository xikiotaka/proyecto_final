from django.db import models

class AboutUs(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='about/', null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Acerca de Nosotros'
        verbose_name_plural = 'Acerca de Nosotros'

    def __str__(self):
        return self.titulo
