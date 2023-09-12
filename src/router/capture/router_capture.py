# third party
from fastapi import APIRouter, HTTPException, status
from decouple import config
# local
from src.services.capture.services_capture import Capture_Service

router_capture = APIRouter()
collection_pokemons = config('COLLECTION_P')
collection_capture = config('COLLECTION_C')


@router_capture.post("/capture",
                     name='Capturar Pokemon',
                     description='Realiza o vinculo de Treinador ao pokemon desejado.')
async def capture_poke(unique_id: str, number_pokemon: int, name_pokemon: str):
    try:
        Capture_Service.capture_pokemon(collection_capture, collection_pokemons, name_pokemon, unique_id, number_pokemon)
        return ('Captured Sucessful')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router_capture.get("/get_capture",
                    name='Listar captura',
                    description='Lista as inforamções da captura desejada.')
async def get_capture(unique_id: str):
    try:
        capture_get = Capture_Service.get_captures(collection_capture, unique_id)
        return capture_get
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router_capture.get('/skip_limit_capture',
                    name='Paginação de captura',
                    description='Pesquisa paginada de capturas.')
async def pagination_cap(skip: int, limit: int):
    try:
        paginacao_captura = Capture_Service.pagination(collection_capture, skip, limit)
        return paginacao_captura
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router_capture.put('/update_capture',
                    name='Update de captura',
                    description='Realiza alteração de dados de captura já salvos no banco de dados.')
async def update_pok(unique_id: str, name_pokemon: str):
    try:
        update_capture = Capture_Service.update_name(unique_id, name_pokemon)
        return ('UPdate sucess')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router_capture.delete('/delete_capture',
                       name='Deletar Capture')
async def delete_cap(unique_id: str):
    try:
        delete_capture = Capture_Service.delete_cap(unique_id)
        return (f'{delete_capture} OK!')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
