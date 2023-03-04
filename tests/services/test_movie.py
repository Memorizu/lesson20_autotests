import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(2)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert type(movies) == list

    def test_create(self):
        movie_data = {
            'title': 'Чикаго',
            'description': 'test',
            'trailer': 'test',
            'year': '2000',
            'rating': '7.6',
            'genre_id': '4',
            'director_id': '1'
        }
        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_update(self):
        movie_data = {
            'id': '1',
            'title': 'Чикаго',
            'description': 'test',
            'trailer': 'test',
            'year': '2000',
            'rating': '7.6',
            'genre_id': '4',
            'director_id': '1'
        }
        movie = self.movie_service.update(movie_data)
        assert movie.id is not None

    def test_delete(self):
        movie = self.movie_service.delete(2)
        assert movie is None
