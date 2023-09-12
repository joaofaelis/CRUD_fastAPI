# Third Party
from fastapi import APIRouter, HTTPException, status
from decouple import config
# Local
from src.services.pokemons.services_pokemons import Service_Pokemon

router_pokemons = APIRouter()
collection_db = config('COLLECTION_P')


@router_pokemons.get("/get_pokemon",
                     name="Pesquisa de Pokemons",
                     description="Utilizar números para pesquisar pokemons.")
async def get_pokemon(number_pokemon: int):
    try:
        get_pokemon = Service_Pokemon.get_api_pokemon(number_pokemon)
        return get_pokemon
    except KeyError:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= 'Verifique se o número é válido.'
        )


@router_pokemons.get("/skip_limit_pokemon",
                     name="Paginação de Pokemon",
                     description="Pesquisa paginada de pokemons.")
async def skip_limit_pokemon(skip: int, limit: int):
    try:
        pagination = Service_Pokemon.pagination(collection_db, skip, limit)
        return pagination
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Certifique que o número de Skip ou Limit é válido...')


@router_pokemons.post("/insert_pokemon",
                      name='Criação de Pokemons',
                      description='Registro de criação de pokemons no Banco de dados.')
async def insert_pokemon(number_pokemon: int):
    try:
        insert_pokemons = Service_Pokemon.insert_pokemon(collection_db, number_pokemon)
        return (f'{insert_pokemons} Created!')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router_pokemons.delete("/delete_pokemon",
                        name='Deletar Pokemons',
                        description='Excluir pokemons criados do banco de dados.')
async def delete_pokemon(unique_id: str):
    try:
        delete = Service_Pokemon.delete_pokemons(collection_db, unique_id)
        return ("Pokemon Deleted")
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router_pokemons.put("/soft_delete_pokmeon",
                     name='Soft Delete',
                     description='O soft delete altera o status do pokemon para False, retirando da lista de paginação.')
async def soft_delete_pokemon(unique_id: str):
    try:
        soft_delete = Service_Pokemon.soft_delete_pokemon(collection_db, unique_id)
        return (f'{soft_delete} ALtered (False).')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)



