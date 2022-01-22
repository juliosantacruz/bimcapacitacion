from django.contrib import admin
from .models import Pagina

# Register your models here.
class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'creado') #visualizar columnas

admin.site.register(Pagina, PaginaAdmin)