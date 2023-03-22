from django.shortcuts import render

from filmoteka.queries.movie import get_movie


def movie_info(request, movie_id: int):
    return render(request, 'index.html', {
        'data': get_movie(movie_id)
    })
