"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from filmoteka.views.favourite import add_favourite, remove_favourite
from filmoteka.views.movie import movie, add_comment
from filmoteka.views.index import index, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmoteka/movie/<int:movie_id>', movie, name='movie'),
    path('filmoteka/movie/<int:movie_id>/comment', add_comment, name='add_comment'),
    path('filmoteka/', index, name='index'),
    path('filmoteka/search/', search, name='search'),
    path('filmoteka/favourite/add/<int:movie_id>', add_favourite, name='add_favourite'),
    path('filmoteka/favourite/remove/<int:movie_id>', remove_favourite, name='remove_favourite'),
]
