from django.urls import path, include
from filmoteka.views.favourite import favourite, add_favourite, remove_favourite
from filmoteka.views.movie import movie, add_comment, add_mark, update_mark, remove_mark
from filmoteka.views.index import index, search, Register

urlpatterns = [
    path('movie/<int:movie_id>', movie, name='movie'),
    path('movie/<int:movie_id>/comment', add_comment, name='add_comment'),
    path('movie/<int:movie_id>/mark/add/<int:mark>', add_mark, name='add_mark'),
    path('movie/<int:movie_id>/mark/update/<int:mark>', update_mark, name='update_mark'),
    path('movie/<int:movie_id>/mark/remove', remove_mark, name='remove_mark'),
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('search/', search, name='search'),
    path('favourite/', favourite, name='favourite'),
    path('favourite/add/<int:movie_id>', add_favourite, name='add_favourite'),
    path('favourite/remove/<int:movie_id>', remove_favourite, name='remove_favourite'),
]
