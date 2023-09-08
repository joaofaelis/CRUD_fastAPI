from src.repository.repository import Repository
from src.domain.DTO.schema_docs_mongo import Model_Up, Soft


class Service:

    @classmethod
    def get_trainers(cls, collection, unique_id):
        query = {"unique_id": unique_id}
        get = Repository.get_object(collection, query)
        mongo = {
            "unique_id": get["unique_id"],
            "name": get["name"],
            "age": get["age"],
            "gender": get["gender"],
            "status": get["status"],
            "created_at": get["created_at"]
        }
        return mongo


    @classmethod
    def skip_limit_trainers(cls, collection, skip, limit):
        collection = Repository.get_collection(collection)
        skip_limit = (collection.find({"status": True}).skip(skip).limit(limit))
        return_skip = list(skip_limit)
        final_list = []
        for trainer in return_skip:
            list_new = {
            "unique_id": trainer["unique_id"],
            "name": trainer["name"],
            "age": trainer["age"],
            "gender": trainer["gender"],
            "status": trainer["status"],
            "created_at": trainer["created_at"]
        }
            final_list.append(list_new)
        return_pagination = {"trainer": final_list}
        return return_pagination


    @classmethod
    def update_trainers(cls, collection, unique_id, update: Model_Up):
        update_obj = {"unique_id": unique_id}
        give_obj = Repository.get_object(collection, update_obj)
        up_date = {
                 "name": update.name,
                 "age": update.age,
                 "gender": update.gender,
                 "created_at": update.created_at
        }
        execute_up = Repository.update_object(collection, give_obj, {"$set": up_date})
        return execute_up


    @classmethod
    def delete_trainers(cls, collection, unique_id):
        delete_obj = {"unique_id": unique_id}
        delete = Repository.delete_object(collection, delete_obj)
        return delete


    @classmethod
    def soft_delete(cls, collection, unique_id, soft: Soft):
        select_trainers = {"unique_id": unique_id}
        give_trainer = Repository.get_object(collection, select_trainers)
        soft = {
            "status": soft.status
        }
        soft_delete = Repository.update_object(collection, give_trainer, {"$set": soft})
        return soft_delete






