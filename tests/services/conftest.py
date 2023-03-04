from unittest.mock import MagicMock

import pytest
from dao.model.director import Director
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    horror = Genre(id=1, name='Ужасы')
    anime = Genre(id=2, name='Анимэ')
    comedy = Genre(id=3, name='Комедия')
    detective = Genre(id=4, name='Детектив')

    genre_dao.get_one = MagicMock(return_value=horror)
    genre_dao.get_all = MagicMock(return_value=[horror, anime, comedy, detective])
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.update = MagicMock(return_value=comedy)
    genre_dao.delete = MagicMock(return_value=None)
    genre_dao.partially_update = MagicMock(return_value=None)

    return genre_dao


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    dir_1 = Director(id=1, name='Тейлор Шеридан')
    dir_2 = Director(id=2, name='Квентин Тарантино')
    dir_3 = Director(id=3, name='Дени Вильнёв')

    director_dao.get_one = MagicMock(return_value=dir_1)
    director_dao.get_all = MagicMock(return_value=[dir_1, dir_2, dir_3])
    director_dao.create = MagicMock(return_value=Director(id=1))
    director_dao.update = MagicMock(return_value=dir_1)
    director_dao.delete = MagicMock(return_value=None)
    director_dao.partially_update = MagicMock(return_value=None)

    return director_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Чикаго', description='тест', trailer='test', year=2000, rating=7.6, genre_id=4, director_id=1)
    movie_2 = Movie(id=2, title='Интерстеллар', description='тест', trailer='test', year=2018, rating=7.6, genre_id=4, director_id=1)
    movie_3 = Movie(id=3, title='Властелин Колец', description='тест', trailer='test', year=2010, rating=7.6, genre_id=4, director_id=1)

    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.update = MagicMock(return_value=movie_3)
    movie_dao.delete = MagicMock(return_value=None)

    return movie_dao
