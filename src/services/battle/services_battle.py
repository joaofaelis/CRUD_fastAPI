# local
from src.repository.mongo.repository_mongo import RepositoryMongo
from uuid import uuid4
from datetime import datetime
# third party
from decouple import config

class Service_Battle:



    @classmethod
    def battle(cls, pokemon_id_one, pokemons_id_two, collection):
        query_pokemon_one: dict = {"pokemon_id": pokemon_id_one}
        query_pokemon_two: dict = {"pokemon_id": pokemons_id_two}
        battle_object_one: dict = RepositoryMongo.get_object("captures", query_pokemon_one)
        battle_object_two: dict = RepositoryMongo.get_object("captures", query_pokemon_two)
        if battle_object_one["experience"] > battle_object_two["experience"]:
            trainer_winner_unique_id = battle_object_one
            poke_battle = {
                "id_winner_battle": str(uuid4()),
                "trainer_winner_id": trainer_winner_unique_id,
                "pokemon_id": battle_object_one["pokemon_id"],
                "pokemon": battle_object_one["pokemon"],
                "number_pokemon": battle_object_one["number_pokemon"],
                "name_pokemon": battle_object_one["name_pokemon"],
                "weight": battle_object_one["weight"],
                "experience": battle_object_one["experiencie"],
                "date_battle": str(datetime.now()),
            }

        else:
            trainer_winner_unique_id = battle_object_two
            poke_battle = {
                "id_winner_battle": str(uuid4()),
                "trainer_winner_id": trainer_winner_unique_id,
                "poke_id": battle_object_two["poke_id"],
                "pokemon": battle_object_two["pokemon"],
                "number_pokemon": battle_object_two["number_pokemon"],
                "name_pokemon": battle_object_two["name_pokemon"],
                "weight": battle_object_two["weight"],
                "experience": battle_object_two["experience"],
                "date_battle": str(datetime.now()),
            }

        RepositoryMongo.insert_object(collection, poke_battle)
        return poke_battle