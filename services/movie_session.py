from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date is None:
        return MovieSession.objects.all()
    else:
        session_date = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.date = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = get_movie_session_by_id(session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_movie_session_by_id(session_id)
    movie_session.delete()
