from django.contrib import admin
from .models import Usuario


admin.site.register(Usuario)

class usuarioCustom(admin.ModelAdmin):
    list_filter = ('id',)