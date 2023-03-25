from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from filmoteka.queries.favourite import add_to_favourite, remove_from_favourite, get_my_favourite_movies


@login_required()
def favourite(request):
    return render(request, 'favourite.html', {
        'movies': get_my_favourite_movies(request.user.id),
    })


@login_required
def add_favourite(request, movie_id: int):
    add_to_favourite(request.user.id, movie_id)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_favourite(request, movie_id: int):
    remove_from_favourite(request.user.id, movie_id)
    return redirect(request.META.get('HTTP_REFERER'))
