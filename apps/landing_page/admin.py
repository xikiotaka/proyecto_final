from django.contrib import admin
from .models import LandingPage
from .models import Categoria
from .models import Noticia

admin.site.register(LandingPage)
admin.site.register(Categoria)
admin.site.register(Noticia)
    

class noticiaCustom(admin.ModelAdmin):
    search_fields = ('titulo',)