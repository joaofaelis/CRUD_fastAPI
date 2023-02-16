from fastapi import APIRouter
from src.services.pokemons.services import Service_Pokemon

pokemon = APIRouter()
collection = 'pokemons'


@pokemon.get("/get_pokemon")
async def get_pokemon(number_pokemon: int):
    get = Service_Pokemon.get_api_pokemon(number_pokemon)
    return get

@pokemon.get("/skip_limit_pokemon")
async def skip_limit_pokemon(skip: int, limit: int):
    pagination = Service_Pokemon.pagination(collection, skip, limit)
    return pagination

@pokemon.post("/insert_pokemon")
async def insert_pokemon(number_pokemon: int):
    insert = Service_Pokemon.insert_pokemon(collection, number_pokemon)
    return (f'{insert} Created!')

@pokemon.delete("/delete_pokemon")
async def delete_pokemon(unique_id: str):
    delete = Service_Pokemon.delete_pokemons(collection, unique_id)
    return ("Deleted")

@pokemon.put("/soft_delete_pokmeon")
async def soft_delete_pokemon(unique_id: str):
    soft_delete = Service_Pokemon.soft_delete_pokemon(collection, unique_id)
    return (f'{soft_delete} ALtered(False).')



