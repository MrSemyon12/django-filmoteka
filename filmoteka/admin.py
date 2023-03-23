from django.contrib import admin
from filmoteka.models import Director, Actor, Genre, Movie, Comment, Mark, Favourite

admin.site.register([Director, Actor, Genre, Movie, Comment, Mark, Favourite])
