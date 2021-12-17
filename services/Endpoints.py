from flask_restful import Resource
from services.csv_reader import read_csv
from models.Movie import Movie
from models.Link import Link
from models.Rating import Rating
from models.Tag import Tag


class Movies(Resource):
    def get(self):
        return read_csv('data/movies.csv', Movie)


class Links(Resource):
    def get(self):
        return read_csv('data/links.csv', Link)


class Ratings(Resource):
    def get(self):
        return read_csv('data/ratings.csv', Rating)


class Tags(Resource):
    def get(self):
        return read_csv('data/tags.csv', Tag)
