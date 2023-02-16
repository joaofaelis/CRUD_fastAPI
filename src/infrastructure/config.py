from pymongo import MongoClient

class Infra:
    DB = MongoClient('mongodb://localhost:27017')
    CONECT = DB.get_database('crud_fastapi')








