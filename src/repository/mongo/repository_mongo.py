#local
from src.infrastructure.mongo.mongo_infra import InfraMongoDb

class RepositoryMongo:

    @classmethod
    def get_collection(cls, collection):
        database = InfraMongoDb.get_collection(collection)
        return database

    @classmethod
    def insert_object(cls, collection, object):
        insert_one = cls.get_collection(collection).insert_one(object)
        return insert_one

    @classmethod
    def get_object(cls, collection, unique_id):
        find_object = cls.get_collection(collection)
        find_service = find_object.find_one(unique_id)
        return find_service

    @classmethod
    def update_object(cls, collection, query, object_up):
        collection_db = cls.get_collection(collection)
        update = collection_db.update_one(query, object_up)
        return update

    @classmethod
    def delete_object(cls, collection, unique_id):
        collection_db = cls.get_collection(collection)
        delete_obj = collection_db.delete_one(unique_id)
        return delete_obj

    @classmethod
    def soft_delete(cls, collection, unique_id):
        collection_db = cls.get_collection(collection)
        soft = collection_db.update_one(unique_id)
        return soft

    @classmethod
    def skip_limit(cls, collection, skip, limit):
        collection_db = cls.get_collection(collection)
        skip_limit = collection_db.find({}, {'status': True}).skip(skip).limit(limit)
        result = list(skip_limit)
        return result
