from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags ###Lo puse para evitar ataques de XSS mostrando solamente texto limpio. Para que no puedan introducir scripts dañinos
from django import forms

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    cuerpo = models.TextField()
    calificacion = models.IntegerField()

    class Meta:
        ordering = ('calificacion',)
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'

    def __str__(self):
        return self.cuerpo

    def clean(self):
        self.cuerpo = strip_tags(self.cuerpo)  
        if not self.cuerpo:
            raise ValidationError("El cuerpo del comentario no puede estar vacío.")

class Post(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    subtitulo = models.CharField(max_length=200, null=False, blank=False)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    texto = models.TextField(null=False, blank=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)  ###Ver si vamos a permitir NULL o no, se dejo en null para poder mantener la noticia
    imagen = models.ImageField(upload_to='media', null=False, blank=False, default='static/img/post_default.jpg')
    publicado = models.DateTimeField(auto_now_add=True)
    comentario = models.ManyToManyField(Comentario, blank=True)  

    class Meta:
        ordering = ('publicado',)

    def __str__(self):
        return self.titulo

    def clean(self):
        self.texto = strip_tags(self.texto)  
        if not self.titulo or not self.subtitulo:
            raise ValidationError("El título y el subtítulo son obligatorios.")

    def delete(self, using=None, keep_parents=False):
        if self.imagen:
            self.imagen.delete(save=False)  
        super().delete(using=using, keep_parents=keep_parents)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'

    def __str__(self):
        return f"Like for {self.post.titulo}"
