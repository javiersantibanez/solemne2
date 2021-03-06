# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titular = models.CharField(max_length=140)
    categoria = models.ForeignKey(Categoria)
    description = models.TextField()
    destacada = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.titular


# Create your models here.
