from fastapi import APIRouter
from src.services.capture.services import Capture

capture = APIRouter()
collection = "pokemons"
collection_two = "capture"


@capture.post("/capture")
async def capture_poke(unique_id: str, number_pokemon: int, name_pokemon: str):
    Capture.capture_pokemon(collection_two, collection, name_pokemon, unique_id, number_pokemon)
    return ('Perfect')

@capture.get("/get_capture")
async def get_capture(unique_id: str):
    cap = Capture.get_captures(collection_two, unique_id)
    return cap

@capture.get('/get_cappture')
async def pagination_cap(skip: int, limit: int):
    pag = Capture.pagination_cap(collection_two, skip, limit)
    return pag

@capture.put('/up_cap')
async def update_pok(unique_id: str, name_pokemon: str):
    up = Capture.update_name(unique_id, name_pokemon)
    return ('UPdate sucess')

@capture.delete('/deletecap')
async def delete_cap(unique_id: str):
    delet = Capture.delete_cap(unique_id)
    return (f'{delet} OK!')