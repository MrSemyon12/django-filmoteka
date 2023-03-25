from datetime import datetime
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
            SELECT username, text, date
            FROM
                filmoteka_comment
                JOIN auth_user ON auth_user.id = filmoteka_comment.user_id
            WHERE filmoteka_comment.movie_id = %s
        """, [movie_id])
        data = cursor.fetchall()

    keys = ['username', 'text', 'date']

    return [{k: v for k, v in zip(keys, comment)} for comment in data]


def get_mark(movie_id: int, user_id: int):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT value
            FROM
                filmoteka_mark
            WHERE movie_id = %s AND user_id = %s
        """, [movie_id, user_id])
        data = cursor.fetchall()

    return data[0][0] if data else []


def add_new_mark(mark: tuple):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO filmoteka_mark (movie_id, user_id, value) VALUES (%s, %s, %s)
        """, [*mark])
        connection.commit()


def update_old_mark(mark: tuple):
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE filmoteka_mark
            SET
                value = %s
            WHERE movie_id = %s AND user_id == %s
        """, [*mark])
        connection.commit()


def remove_old_mark(movie_id: int, user_id: int):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM filmoteka_mark WHERE movie_id = %s AND user_id = %s
        """, [movie_id, user_id])
        connection.commit()


def update_rating(movie_id: int):
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE filmoteka_movie
            SET
                rating = (SELECT AVG(value) FROM filmoteka_mark WHERE movie_id = %s)
            WHERE id = %s
        """, [movie_id, movie_id])
        connection.commit()


def add_new_comment(comment: tuple):
    with connection.cursor() as cursor:
        cursor.execute('''
            INSERT INTO filmoteka_comment (movie_id, user_id, text, date) VALUES (%s, %s, %s, %s)
        ''', [*comment, datetime.now()])
        connection.commit()
