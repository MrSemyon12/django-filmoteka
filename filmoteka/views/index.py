from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from filmoteka.queries.favourite import get_favourites
from filmoteka.queries.index import get_top_last_movies, get_top_comments_movies, get_random_movies, get_pattern_movies


def index(request):
    return render(request, 'index.html', {
        'top_last': get_top_last_movies(),
        'top_comments': get_top_comments_movies(),
        'random_movies': get_random_movies(),
        'favourites': get_favourites(request.user.id) if request.user.is_authenticated else [],
    })


def search(request):
    pattern = request.GET.get('pattern')

    return render(request, 'search.html', {
        'movies': get_pattern_movies(f'%{pattern}%'),
        'favourites': get_favourites(request.user.id) if request.user.is_authenticated else [],
        'prev_pat': pattern,
    })


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)
