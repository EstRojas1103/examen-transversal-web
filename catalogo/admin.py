from django.contrib import admin
from .models import Libro, Autor, Categoria, NavItem

# Register your models here.

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(NavItem)