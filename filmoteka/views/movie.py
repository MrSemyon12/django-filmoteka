from django.shortcuts import render, redirect
from filmoteka.queries.movie import get_movie, get_movie_actors, get_comments, add_new_comment
from django.contrib.auth.decorators import login_required


def movie(request, movie_id: int):
    return render(request, 'movie.html', {
        'movie': get_movie(movie_id),
        'actors': get_movie_actors(movie_id),
        'comments': get_comments(movie_id),
    })


@login_required
def add_comment(request, movie_id: int):
    add_new_comment((movie_id, request.user.id, request.POST['text'].strip()))
    return redirect(request.META.get('HTTP_REFERER'))
