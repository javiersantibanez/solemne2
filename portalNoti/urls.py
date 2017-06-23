from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.noticia_list, name = 'noticia_list'),
	url(r'^noticia/(?P<pk>[0-9]+)/$', views.noticia_detalle, name = 'noticia_detalle'),

   ]