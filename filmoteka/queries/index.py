from django.db import connection


def get_top_last_movies():
    '''Фильмы с самым высоким рейтингом, сортировка по году.'''
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT filmoteka_movie.id, title, year, poster_url, rating, group_concat(DISTINCT filmoteka_movie_genres.genre_id) AS genres
            FROM
                filmoteka_movie
                JOIN filmoteka_movie_genres ON filmoteka_movie_genres.movie_id = filmoteka_movie.id
            GROUP BY filmoteka_movie.id
            ORDER BY year DESC, rating DESC
            LIMIT 6
        ''')
        data = cursor.fetchall()

    keys = ['id', 'title', 'year', 'poster_url', 'rating', 'genres']

    return [{k: v for k, v in zip(keys, movie)} for movie in data]
