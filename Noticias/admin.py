# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Noticias.models import Noticia, Categoria

class NoticiaAdmin (admin.ModelAdmin):
	list_display = ('id','titular','categoria')


class CategoriaAdmin (admin.ModelAdmin):
	pass

admin.site.register(Noticia,NoticiaAdmin)
admin.site.register(Categoria,CategoriaAdmin)

# Register your models here.
