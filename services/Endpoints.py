from flask_restful import Resource
from services.csv_reader import read_csv
from models.Movie import Movie
from models.Links import Links


class Movies(Resource):
    def get(self):
        return read_csv('data/movies.csv', Movie)


class Links(Resource):
    def get(self):
        return read_csv('data/links.csv', Links)


class Ratings(Resource):
    def get(self):
        return read_csv()


class Tags(Resource):
    def get(self):
        return read_csv()
