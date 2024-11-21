from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'contrasena')  # Ajustar los nombres a los definidos en el modelo

admin.site.register(Usuario, UsuarioAdmin)
