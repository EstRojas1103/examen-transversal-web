from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.libros, name='libros'),
    path('autores/', views.autores, name='autores'),
    path('categorias/', views.categorias, name='categorias'),
    path('libro/<int:libro_id>/', views.libro_detalle, name='libro_detalle'), 
]
