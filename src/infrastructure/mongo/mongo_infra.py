#third party
from pymongo import MongoClient
from decouple import config
from pymongo.collection import Collection

class InfraMongoDb:

    __connections = dict()

    @staticmethod
    def __create_client() -> MongoClient:
        host = config("MONGO_HOST")
        client = MongoClient(host=host)
        return client

    @classmethod
    def __create_connection(cls, collection_name: str) -> Collection:
        database_name = config("MONGO_DATABASE")
        client = cls.__create_client()
        db_connection = client[database_name]
        collection = db_connection[collection_name]
        return collection

    @classmethod
    def get_collection(cls, collection_name: str) -> Collection:
        if collection_name not in cls.__connections:
            collection = cls.__create_connection(collection_name=collection_name)
            cls.__connections[collection_name] = collection
            return cls.__connections[collection_name]





