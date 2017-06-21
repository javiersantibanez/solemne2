from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.noticia_list, name = 'noticia_list'),
   ]