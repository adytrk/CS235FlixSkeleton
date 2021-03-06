from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watchlist = []

    @property
    def watchlist(self):
        return self.__watchlist;

    def add_movie(self, movie: Movie):
        if movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        try:
            return self.__watchlist[index]
        except IndexError:
            return None

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) > 0:
            return self.__watchlist[0]
        return None

    def __iter__(self):
        self.__n = 0
        return self

    def __next__(self):
        if self.__n <= self.size() - 1:
            result = self.__watchlist[self.__n]
            self.__n += 1
            return result
        else:
            raise StopIteration


class TestWatchlistMethods:

    def test_init(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        assert watchlist.size() == 1
        watchlist.remove_movie(Movie("Moana", 2016))
        assert watchlist.size() == 0

        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        movie = watchlist.select_movie_to_watch(100)
        assert movie is None

        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        movie = watchlist.select_movie_to_watch(100)
        assert movie is None

        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        movie = watchlist.select_movie_to_watch(0)
        assert movie == "<Movie Moana, 2016>"

        watchlist = WatchList()
        assert watchlist.size() == 0
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        assert watchlist.first_movie_in_watchlist() == "<Movie Moana, 2016>"
