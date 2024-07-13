from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    anio_publicacion = models.IntegerField()
    descripcion_breve = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo

class NavItem(models.Model):
    titulo = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo