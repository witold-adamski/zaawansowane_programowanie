class Rating:
    def __init__(self, userId: str, movieId: str, rating: str, timestamp: str):
        self._userId = userId
        self._movieId = movieId
        self._rating = rating
        self._timestamp = timestamp

    def api(self):
        return {'userId': self._userId,
                'movieId': self._movieId,
                'rating': self._rating,
                'timestamp': self._timestamp}
