import datetime

from django.db import connection


def get_favourites(user_id: int):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT filmoteka_movie.id
            FROM
                filmoteka_movie                
                JOIN filmoteka_favourite ON filmoteka_movie.id = filmoteka_favourite.movie_id
            WHERE filmoteka_favourite.user_id = %s
            GROUP BY filmoteka_movie.id
            ORDER BY filmoteka_favourite.date DESC
        ''', [user_id])
        data = cursor.fetchall()

    return [x[0] for x in data]


def add_to_favourite(user_id: int, movie_id: int):
    with connection.cursor() as cursor:
        cursor.execute('''
            INSERT INTO filmoteka_favourite (user_id, movie_id, date) VALUES (%s, %s, %s)
        ''', [user_id, movie_id, datetime.datetime.now()])
        connection.commit()


def remove_from_favourite(user_id: int, movie_id: int):
    with connection.cursor() as cursor:
        cursor.execute('''
            DELETE FROM filmoteka_favourite WHERE user_id = %s AND movie_id = %s
        ''', [user_id, movie_id])
        connection.commit()
