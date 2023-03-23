from django.db import connection


def get_movie(movie_id: int):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT filmoteka_movie.id, title, year, poster_url, filmoteka_director.name, photo_url, group_concat(DISTINCT filmoteka_movie_genres.genre_id) AS genres, rating, country, description, duration
            FROM
                filmoteka_movie
                JOIN filmoteka_director ON filmoteka_movie.director_id = filmoteka_director.id
                JOIN filmoteka_movie_genres ON filmoteka_movie_genres.movie_id = filmoteka_movie.id                
            WHERE filmoteka_movie.id = %s
            GROUP BY filmoteka_movie.id
        ''', [movie_id])
        data = cursor.fetchall()

    keys = ['id', 'title', 'year', 'poster_url', 'director', 'photo_url', 'genres', 'rating', 'country', 'description',
            'duration']

    return {k: v for k, v in zip(keys, data[0])}


def get_movie_actors(movie_id: int):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT name, photo_url
            FROM
                filmoteka_movie
                JOIN filmoteka_movie_actors ON filmoteka_movie_actors.movie_id = filmoteka_movie.id
                JOIN filmoteka_actor ON filmoteka_movie_actors.actor_id = filmoteka_actor.id 
            WHERE movie_id == %s
        ''', [movie_id])
        data = cursor.fetchall()

    keys = ['name', 'photo_url']

    return [{k: v for k, v in zip(keys, actor)} for actor in data]


def get_comments(movie_id: int):
    with connection.cursor() as cursor:
        cursor.execute("""

        """, [movie_id])
        data = cursor.fetchall()

    keys = ['id', 'title', 'year', 'poster_url', 'director', 'photo_url', 'genres', 'rating', 'country', 'description',
            'duration']

    return {k: v for k, v in zip(keys, data[0])}
