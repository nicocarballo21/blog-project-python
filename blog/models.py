from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    creada = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="Blog", null=True, blank=True)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # cuando se elimina un usuario se elimianan sus post
    categorias = models.ManyToManyField(
        Categorias
    )  # cada cat puede tener varios post y cada post puede tener varias categorias
    creado = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
