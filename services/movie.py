from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None,
) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,

) -> Movie:
    if not genres_ids and not actors_ids:
        return Movie.objects.create(
            title=movie_title,
            description=movie_description
        )

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)

    return movie
