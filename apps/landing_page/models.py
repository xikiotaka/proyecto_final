from django.db import models

class LandingPage(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.TextField()
    contenido = models.TextField()
    imagen_destacada = models.ImageField(upload_to='landing/', null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Landing Page'
        verbose_name_plural = 'Landing Pages'

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=255, blank=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_publicacion']  ###Ordené las noticias de la nueva a la más antigua.
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo
