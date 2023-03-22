from django.db import connection


def get_movie(movie_id: int):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT filmoteka_movie.id, title, year, poster_url, filmoteka_director.name, photo_url, group_concat(DISTINCT filmoteka_genre.name) AS genres, rating, country, description, duration
            FROM
                filmoteka_movie
                JOIN filmoteka_director ON filmoteka_movie.director_id = filmoteka_director.id
                JOIN filmoteka_movie_genres ON filmoteka_movie_genres.movie_id = filmoteka_movie.id
                JOIN filmoteka_genre ON filmoteka_movie_genres.genre_id = filmoteka_genre.name
            WHERE filmoteka_movie.id = %s
            GROUP BY filmoteka_movie.id
        """, [movie_id])
        result = cursor.fetchall()

    return result[0]
