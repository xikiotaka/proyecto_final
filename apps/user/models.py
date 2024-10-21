from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.exceptions import ValidationError

# Validador personalizado para limitar el tamaño máximo de la imagen a 5 MB
def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # Define el tamaño máximo permitido (5 MB)
    if image.size > max_size:
        raise ValidationError("La imagen es demasiado grande. Tamaño máximo: 5 MB.")

# Definición del modelo Usuario personalizado basado en AbstractUser
class Usuario(AbstractUser):
    ###El campo de email será único y se usará como identificador principal
    email = models.EmailField(unique=True)  

    # Campo de imagen de perfil opcional, con un valor por defecto y validación de tamaño
    imagen = models.ImageField(
        upload_to='usuarios/',  ###Carpeta donde se guardan las imágenes
        null=True,              ##Permitido que sea nulo (sin imagen)
        blank=True,             ###Permitido que quede en blanco (sin imagen)
        default='usuarios/user-default.jpg',  ###Imagen predeterminada
        validators=[validate_image_size]      
    )

    # Campo para gestionar la relación del usuario con grupos (roles) en Django
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_usuario_groups',  # Nombre relacionado para consultas
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.',  # Texto de ayuda en el admin
        related_query_name='usuario',  # Nombre para realizar consultas relacionadas
    )

    # Campo para gestionar permisos específicos asignados a cada usuario
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_usuario_permissions',  # Nombre relacionado para consultas
        blank=True,
        help_text='Permisos específicos para este usuario.',  # Texto de ayuda en el admin
        related_query_name='usuario',  # Nombre para consultas relacionadas
    )

    # Definición del campo que será utilizado como nombre de usuario (login)
    USERNAME_FIELD = 'email'  # El usuario iniciará sesión usando el email

    # Lista de campos requeridos además del email, en este caso vacío (sin campos obligatorios adicionales)
    REQUIRED_FIELDS = []  

    # Método que retorna la URL absoluta del perfil del usuario (redirige a 'index')
    def get_absolute_url(self):
        return reverse('index')  

    # Representación en cadena del usuario, devuelve el email
    def __str__(self):
        return self.email

    # Método para obtener el nombre completo del usuario
    def get_full_name(self):
        # Combina el nombre y apellido, eliminando posibles espacios en blanco
        return f"{self.first_name} {self.last_name}".strip()
