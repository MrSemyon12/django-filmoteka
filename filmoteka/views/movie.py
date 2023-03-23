from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from filmoteka.queries.movie import get_movie, get_movie_actors, get_comments


def movie(request, movie_id: int):
    return render(request, 'movie.html', {
        'movie': get_movie(movie_id),
        'actors': get_movie_actors(movie_id),
        'comments': [],
    })
