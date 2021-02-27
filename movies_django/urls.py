"""movies_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import index
from Movies.views import new_movie,get_all_movies,get_movie,get_detail_movie,edit_movie,delete_movie
from Categorias.views import get_all_categories,nueva_categoria,editar_categoria,eliminar_categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('',get_all_movies,name='inicio'),
    path('peliculas/nueva_pelicula',new_movie,name='nueva_pelicula'),
    path('peliculas/',get_detail_movie,name='detail_movies'),
    path('peliculas/editar_pelicula/<int:id>',edit_movie),
    path('peliculas/eliminar_pelicula/<int:id>',delete_movie),
    path('watch/<int:id>',get_movie),
    path('categorias/',get_all_categories,name='categorias'),
    path('nueva_categoria/',nueva_categoria,name='new_categorie'),
    path('categorias/editar_categoria/<int:id>',editar_categoria,name='editar_categoria'),
    path('categorias/eliminar_categoria/<int:id>',eliminar_categoria)
]
