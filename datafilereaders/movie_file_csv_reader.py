import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                actors_list = row['Actors']
                director = row['Director']
                genres_list = row['Genre']

                movie = Movie(title, release_year)
                if movie not in self.__dataset_of_movies:
                    self.__dataset_of_movies.append(movie)

                for actor in actors_list.split(','):
                    if Actor(actor) not in self.__dataset_of_actors:
                        self.__dataset_of_actors.add(Actor(actor))

                if Director(director) not in self.__dataset_of_directors:
                    self.__dataset_of_directors.add(Director(director))

                for genre in genres_list.split(','):
                    if Genre(genre) not in self.__dataset_of_genres:
                        self.__dataset_of_genres.add(Genre(genre))

