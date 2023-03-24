from django.shortcuts import render

from filmoteka.queries.favourite import get_favourites
from filmoteka.queries.index import get_top_last_movies, get_top_comments_movies, get_random_movies, get_pattern_movies


def index(request):
    return render(request, 'index.html', {
        'top_last': get_top_last_movies(),
        'top_comments': get_top_comments_movies(),
        'random_movies': get_random_movies(),
        'favourites': get_favourites(request.user.id) if request.user.is_authenticated else []
    })


def search(request):
    pattern = request.POST['pattern'].strip()

    return render(request, 'search.html', {
        'movies': get_pattern_movies(f'%{pattern}%'),
        'favourites': get_favourites(request.user.id) if request.user.is_authenticated else [],
        'prev_pat': pattern
    })
