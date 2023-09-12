# local
from src.repository.mongo.repository_mongo import RepositoryMongo
from src.services.pokemons.services_pokemons import Service_Pokemon
from uuid import uuid4
from datetime import datetime



class Capture_Service(Service_Pokemon):

    @classmethod
    def capture_pokemon(cls, collection_capture, collection_pokemon, name_pokemon, unique_id, number_pokemon):
        object_find = {'number_pokemon': number_pokemon}
        get_info: dict = RepositoryMongo.get_object(collection_pokemon, object_find)
        if get_info is None:
            pokemon_objects: dict = Service_Pokemon.get_api_pokemon(number_pokemon)
            pokemon_objects.update({
                "unique_id": str(uuid4()),
                "trainer_id": unique_id,
                "pokemon_id": str(uuid4()),
                "number_pokemon": number_pokemon,
                "name_pokemon": name_pokemon,
                "weight": pokemon_objects['weight'],
                "experience": pokemon_objects['experience'],
                "captured_in": str(datetime.now()),
                "status": True,
                "created_at": str(datetime.now())

            })
            RepositoryMongo.insert_object(collection_capture, pokemon_objects)
            return pokemon_objects
        else:
            get_info.update({
                "unique_id": str(uuid4()),
                "trainer_id": unique_id,
                "pokemon_id": get_info["unique_id"],
                "number_pokemon": get_info["number_pokemon"],
                "name_pokemon": name_pokemon,
                "weight": get_info['weight'],
                "experience": get_info['experience'],
                "captured_in": str(datetime.now())
            }
            )
            RepositoryMongo.insert_object(collection_capture, get_info)
            return get_info

    @classmethod
    def get_captures(cls, collection, unique_id):
        query = {"unique_id": unique_id}
        capture_find = RepositoryMongo.get_object(collection, query)
        obj_captured = {
            "unique_id": capture_find['unique_id'],
            "trainer_id": capture_find['trainer_id'],
            "pokemon_id": capture_find['pokemon_id'],
            "pokemon": capture_find['pokemon'],
            "number_pokemon": capture_find['number_pokemon'],
            "name_pokemon": capture_find['name_pokemon'],
            "weight": capture_find['weight'],
            "experience": capture_find['experience'],
            "captured_in": capture_find['captured_in'],
            "status": capture_find['status'],
            "created_at": capture_find['created_at']
        }
        return obj_captured

    @classmethod
    def pagination_capture(cls, collection, skip, limit):
        collection_db = RepositoryMongo.get_collection(collection)
        skip_limit = (collection_db.find({"status": True}).skip(skip).limit(limit))
        return_skip = list(skip_limit)
        final_list = []
        for captured in return_skip:
            list_new = {
            "unique_id": captured['unique_id'],
            "trainer_id": captured['trainer_id'],
            "pokemon_id": captured['pokemon_id'],
            "pokemon": captured['pokemon'],
            "number_pokemon": captured['number_pokemon'],
            "name_pokemon": captured['name_pokemon'],
            "weight": captured['weight'],
            "experience": captured['experience'],
            }
            final_list.append(list_new)
        return_pagination = {"pokemon": final_list}
        return return_pagination

    @classmethod
    def update_name(cls, unique_id, name_pokemon):
        update_obj = {"unique_id": unique_id}
        give_obj = RepositoryMongo.get_object('capture', update_obj)
        up_date = {
            "name_pokemon": name_pokemon,
        }
        execute_up = RepositoryMongo.update_object('capture', give_obj, {"$set": up_date})
        return execute_up


    @classmethod
    def delete_cap(cls, unique_id):
        select = {'unique_id': unique_id}
        delete = RepositoryMongo.delete_object('capture', select)
        return delete
