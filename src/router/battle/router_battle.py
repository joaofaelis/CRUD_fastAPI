# Third Party
from fastapi import APIRouter, HTTPException, status
from decouple import config
# local
from src.services.battle.services_battle import Service_Battle


router_battle = APIRouter()
collection_db = config('COLLECTION_B')


@router_battle.post("/battle_pokemons",
                    name='Batalha de Pokemons',
                    description='Realiza a batalha de pokemons de acordo com a experiência de cada um.')
async def battle_pokemons(id_pokemon_first, id_pokemon_second, collection: collection_db):
    try:
        battle_pokemons = Service_Battle.battle(pokemon_id_one=id_pokemon_first,
                                            pokemons_id_two=id_pokemon_second,
                                            collection=collection)
        return battle_pokemons
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
