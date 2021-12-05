class Movie:
    def __init__(self, id: str, title: str, genres: str):
        self._id = id
        self._title = title
        self._genres = genres

    def api(self):
        return {'id': self._id,
                'title': self._title,
                'genres': self._genres}
