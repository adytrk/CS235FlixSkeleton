from datetime import datetime

from domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = movie
        self.__review_text = review_text
        if 10 >= rating >= 0:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now()

    @property
    def movie(self) -> str:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie}, {self.rating}>"

    def __eq__(self, other):
        return (self.__movie, self.__review_text, self.__rating, self.__timestamp) == (other.movie, other.review_text, other.rating, other.timestamp)
