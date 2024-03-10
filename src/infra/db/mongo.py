""" MongoDB Database module """
from pymongo import MongoClient


def get_database():
    """ Get the MongoDB database """

    client = MongoClient('localhost', 27017)
    return client.get_database('main')
