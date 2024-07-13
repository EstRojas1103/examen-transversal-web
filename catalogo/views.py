from django.shortcuts import render
from .models import Libro, Autor, Categoria
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def inicio(request):
    return render(request, 'catalogo/inicio.html')

def libros(request):
    query = request.GET.get('q')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()
    return render(request, 'catalogo/libros.html', {'libros': libros, 'query': query})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autores.html', {'autores': autores})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/categorias.html', {'categorias': categorias})

def libro_detalle(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    data = {
        'titulo': libro.titulo,
        'anio_publicacion': libro.anio_publicacion,
        'descripcion_breve': libro.descripcion_breve,
        'categoria': libro.categoria.nombre,
        'autores': [autor.nombre for autor in libro.autores.all()]
    }
    return JsonResponse(data)