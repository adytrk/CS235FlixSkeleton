from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, user_name: str, password: str):
        user_name = user_name.strip().lower()
        self.__user_name = user_name
        self.__password = password
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, name):
        self.__user_name = name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, watched_movies):
        self.__watched_movies = watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews):
        self.__reviews = reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent_watching_movies_minutes):
        self.__time_spent_watching_movies_minutes = time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.user_name

    def __lt__(self, other):
        return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        self.__reviews.append(review)
