from django.shortcuts import render, redirect
from filmoteka.queries.favourite import get_favourites
from filmoteka.queries.movie import get_movie, get_movie_actors, get_comments, add_new_comment, get_mark, add_new_mark, \
    update_old_mark, remove_old_mark, update_rating
from django.contrib.auth.decorators import login_required


def movie(request, movie_id: int):
    return render(request, 'movie.html', {
        'movie': get_movie(movie_id),
        'actors': get_movie_actors(movie_id),
        'comments': get_comments(movie_id),
        'favourites': get_favourites(request.user.id) if request.user.is_authenticated else [],
        'mark': get_mark(movie_id, request.user.id) if request.user.is_authenticated else [],
        'marks': [i for i in range(1, 11)],
    })


@login_required
def add_comment(request, movie_id: int):
    add_new_comment((movie_id, request.user.id, request.POST.get('text').strip()))
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def add_mark(request, movie_id: int, mark: int):
    add_new_mark((movie_id, request.user.id, mark))
    update_rating(movie_id)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def update_mark(request, movie_id: int, mark: int):
    update_old_mark((mark, movie_id, request.user.id))
    update_rating(movie_id)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_mark(request, movie_id: int):
    remove_old_mark(movie_id, request.user.id)
    update_rating(movie_id)
    return redirect(request.META.get('HTTP_REFERER'))
