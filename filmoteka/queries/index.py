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


def get_top_comments_movies():
    '''Фильмы с наибольшим количеством комментариев.'''
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT movie_idx, title, year, poster_url, rating, group_concat(DISTINCT filmoteka_movie_genres.genre_id) AS genres
            FROM
                (
                    SELECT filmoteka_movie.id AS movie_idx, title, year, poster_url, rating, count(text) as cnt
                    FROM
                        filmoteka_movie
                        LEFT JOIN filmoteka_comment ON filmoteka_comment.movie_id = filmoteka_movie.id
                    GROUP BY filmoteka_movie.id
                    ORDER BY cnt DESC, rating DESC
                    LIMIT 6
                )
                JOIN filmoteka_movie_genres ON filmoteka_movie_genres.movie_id = movie_idx
            GROUP BY movie_idx
            ORDER BY cnt DESC, rating DESC
        ''')
        data = cursor.fetchall()

    keys = ['id', 'title', 'year', 'poster_url', 'rating', 'genres']

    return [{k: v for k, v in zip(keys, movie)} for movie in data]


def get_random_movies():
    '''Случайный набор фильмов.'''
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT filmoteka_movie.id, title, year, poster_url, rating, group_concat(DISTINCT filmoteka_movie_genres.genre_id) AS genres
            FROM
                filmoteka_movie
                JOIN filmoteka_movie_genres ON filmoteka_movie_genres.movie_id = filmoteka_movie.id
            GROUP BY filmoteka_movie.id
            ORDER BY RANDOM()
            LIMIT 6
        ''')
        data = cursor.fetchall()

    keys = ['id', 'title', 'year', 'poster_url', 'rating', 'genres']

    return [{k: v for k, v in zip(keys, movie)} for movie in data]


def get_pattern_movies(pattern: str):
    '''Поиск фильмов по паттерну.'''
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT DISTINCT filmoteka_movie.id, title, year, poster_url, rating, group_concat(DISTINCT filmoteka_movie_genres.genre_id) AS genres
        FROM
            filmoteka_movie
            JOIN filmoteka_movie_genres ON filmoteka_movie_genres.movie_id = filmoteka_movie.id
        WHERE filmoteka_movie.id IN (
            SELECT filmoteka_movie.id
            FROM
                filmoteka_movie
            WHERE LOWER(title) LIKE LOWER(%s)
            UNION
            SELECT filmoteka_movie.id
            FROM
                filmoteka_movie
                JOIN filmoteka_movie_genres ON filmoteka_movie_genres.movie_id = filmoteka_movie.id
            WHERE LOWER(filmoteka_movie_genres.genre_id) LIKE LOWER(%s)
            UNION
            SELECT filmoteka_movie.id
            FROM
                filmoteka_movie
                JOIN filmoteka_director ON filmoteka_movie.director_id = filmoteka_director.id
            WHERE LOWER(filmoteka_director.name) LIKE LOWER(%s)
            UNION
            SELECT filmoteka_movie.id
            FROM
                filmoteka_movie
                JOIN filmoteka_movie_actors ON filmoteka_movie_actors.movie_id = filmoteka_movie.id
                JOIN filmoteka_actor ON filmoteka_movie_actors.actor_id = filmoteka_actor.id
            WHERE LOWER(filmoteka_actor.name) LIKE LOWER(%s)
            UNION
            SELECT filmoteka_movie.id
            FROM
                filmoteka_movie
            WHERE LOWER(country) LIKE LOWER(%s)
            UNION
            SELECT filmoteka_movie.id
            FROM
                filmoteka_movie
            WHERE year LIKE LOWER(%s)
        )
        GROUP BY filmoteka_movie.id
        ''', [pattern] * 6)
        data = cursor.fetchall()

    keys = ['id', 'title', 'year', 'poster_url', 'rating', 'genres']

    return [{k: v for k, v in zip(keys, movie)} for movie in data]
