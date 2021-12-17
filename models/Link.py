class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self._movieId = movieId
        self._imdbId = imdbId
        self._tmdbId = tmdbId

    def api(self):
        return {'movieId': self._movieId,
                'imdbId': self._imdbId,
                'tmdbId': self._tmdbId}
