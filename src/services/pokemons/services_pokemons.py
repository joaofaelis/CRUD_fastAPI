# Local
from src.repository.mongo.repository_mongo import RepositoryMongo
from uuid import uuid4
from datetime import datetime
# Third Party
import requests


class Service_Pokemon:

    @classmethod
    def get_api_pokemon(cls, number_pokemon):
        number_pokemon = number_pokemon
        api = f'https://pokeapi.co/api/v2/pokemon/{number_pokemon}'
        list_pokemon = requests.get(api)
        result_list = list_pokemon.json()

        final_list = {
            "number_pokemon": number_pokemon,
            "pokemon": result_list["name"],
            "weight": result_list["weight"],
            "experience": result_list["base_experience"],
        }
        return final_list

    @classmethod
    def pagination(cls, collection, skip, limit):
        collection = RepositoryMongo.get_collection(collection)
        skip_limit = (collection.find({"status": True}).skip(skip).limit(limit))
        return_skip = list(skip_limit)
        final_list = []
        for pokemon in return_skip:
            list_new = {
                "number_pokemon": pokemon["number_pokemon"],
                "pokemon": pokemon["pokemon"],
                "weight": pokemon["weight"],
                "experience": pokemon["experience"],
                "unique_id": pokemon["unique_id"],
                "created_at": pokemon["created_at"]
            }
            final_list.append(list_new)
        return_pagination = {"pokemon": final_list}
        return return_pagination

    @classmethod
    def insert_pokemon(cls, collection, insert):
        num_pokemon = insert
        query: dict = {
            "number_pokemon": num_pokemon
        }
        pokemon_objects: dict = RepositoryMongo.get_object(collection, query)
        if pokemon_objects is None:
            pokemon_objects: dict = cls.get_api_pokemon(insert)
            pokemon_objects.update({
                "unique_id": str(uuid4()),
                "status": True,
                "created_at": str(datetime.now())

            })
            RepositoryMongo.insert_object(collection, pokemon_objects)
        return pokemon_objects

    @classmethod
    def delete_pokemons(cls, collection, unique_id):
        select_pokemons = {"unique_id": unique_id}
        delete_pokemon = RepositoryMongo.delete_object(collection, select_pokemons)
        return delete_pokemon

    @classmethod
    def soft_delete_pokemon(cls, collection, unique_id):
        query = {"unique_id": unique_id}
        delete = {"$set": {"status": False}}
        delete_pokemon = RepositoryMongo.update_object(collection, query, delete)
        return delete_pokemon