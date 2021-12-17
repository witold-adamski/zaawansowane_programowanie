class Tag:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: str):
        self._userId = userId
        self._movieId = movieId
        self._tag = tag
        self._timestamp = timestamp

    def api(self):
        return {'userId': self._userId,
                'movieId': self._movieId,
                'tag': self._tag,
                'timestamp': self._timestamp}
