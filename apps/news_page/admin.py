from django.contrib import admin
from .models import Comentario
from .models import Categoria
from .models import Post
from .models import Like

admin.site.register(Comentario)
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Like)

class comentarioCustom(admin.ModelAdmin):
    list_filter = ('id',)
    

class postCustom(admin.ModelAdmin):
    search_fields = ('titulo',)