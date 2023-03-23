from django.shortcuts import render

from filmoteka.queries.favourite import get_favourites
from filmoteka.queries.index import get_top_last_movies


def index(request):
    return render(request, 'index.html', {
        'top_last': get_top_last_movies(),
        'favourites': get_favourites(request.user.id) if request.user.is_authenticated else []
    })
