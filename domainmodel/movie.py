from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, title: str, release_year: int):
        self.__title = None
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__time = None

        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year >= 1900:
            self.__release_year = release_year
        else:
            self.__release_year = None

    # Getters and Setters
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, name):
        self.__title = name

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, year):
        self.__release_year = year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, text):
        self.__description = text

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, actors):
        self.__actors = actors

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, genre):
        self.__genres = genre

    @property
    def runtime_minutes(self) -> int:
        return self.__time

    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if time < 0:
            raise ValueError
        else:
            self.__time = time

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return self.__title == other.__title and self.__release_year == other.__release_year

    def __lt__(self, other):
        if self.__title < other.__title:
            return True
        if self.__release_year < other.__release_year:
            return True
        return False

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    def add_actor(self, actor):
        self.__actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
