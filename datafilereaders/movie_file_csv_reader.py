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
                    movie.genres.append(Genre(genre))
                    if Genre(genre) not in self.__dataset_of_genres:
                        self.__dataset_of_genres.add(Genre(genre))


                rank = row['Rank']
                if int(rank) > 0:
                    movie.rank = rank
                rating = row['Rating']
                if  0 <= float(rating) <= 10:
                    movie.rating = rating
                votes = row['Votes']
                movie.votes = int(votes)
                revenue_millions = row['Revenue (Millions)']
                movie.revenue_millions = revenue_millions
                metascore = row['Metascore']
                try:
                    if 0 <= float(metascore) <= 100:
                        movie.metascore = metascore
                except ValueError:
                    movie.metascore = metascore


    def find_popular_genre(self):
        genres = {}
        for movie in self.__dataset_of_movies:
            for genre in movie.genres:
                if genre in genres:
                    genres[genre] += 1
                else:
                    genres[genre] = 1
        genres_list = sorted(genres.items(), key=lambda x: x[1], reverse=True)
        return genres_list

class TesMovieFileCSVReaderMethods:

    def test_init(self):
        filename = 'Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()
        movie_file_reader.find_popular_genre()
        x = Genre("Drama")
        assert movie_file_reader.find_popular_genre()[0] == (x, 513)

        print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
        print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
        print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
        print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')

