#local
from src.infrastructure.mongo.mongo_infra import InfraMongoDb

database = InfraMongoDb

class Repository:

    @classmethod
    def get_collection(cls, collection):
        datebase = database.get_collection(collection)
        return datebase

    @classmethod
    def insert_object(cls, collection, object):
        insert = cls.get_collection(collection).insert_one(object)
        return insert

    @classmethod
    def get_object(cls, collection, unique_id):
        find = cls.get_collection(collection)
        find_service = find.find_one(unique_id)
        return find_service

    @classmethod
    def update_object(cls, collection, query, object_up):
        collection = cls.get_collection(collection)
        up_trainers = collection.update_one(query, object_up)
        return up_trainers

    @classmethod
    def delete_object(cls, collection, unique_id):
        select_c = cls.get_collection(collection)
        delete_t = select_c.delete_one(unique_id)
        return delete_t

    @classmethod
    def soft_delete(cls, collection, unique_id):
        select_c = cls.get_collection(collection)
        soft = select_c.update_one(unique_id)
        return soft

    @classmethod
    def skip_limit(cls, collection, skip, limit):
        select_c = cls.get_collection(collection)
        skip_limit = select_c.find({}, {'status': True}).skip(skip).limit(limit)
        result = list(skip_limit)
        return result
