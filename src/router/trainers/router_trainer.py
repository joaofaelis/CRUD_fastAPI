# third party
from fastapi import APIRouter, HTTPException, status
from decouple import config
# local
from src.repository.mongo.repository_mongo import RepositoryMongo
from src.services.trainers.services_trainer import Service_Trainer
from src.domain.DTO.schema_docs_mongo import Model_Create, Model_Up, Soft

collection_db = config('COLLECTION_T')
router_trainer = APIRouter()


@router_trainer.get('/Get_trainers',
                    name="Pesquisa de Treinadores no Banco de dados",
                    description="Ao colocar o 'unique_id' do treinador desejado, retornará os dados do mesmo.")
async def get_trainer(unique_id: str):
    try:
        find_trainer = Service_Trainer.get_trainers(collection_db, unique_id)
        return find_trainer
    except KeyError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Verifique novamente se o ID informado está correto...')


@router_trainer.get('/skip_limit',
                    name='Pesquisa paginada de treinadores',
                    description='A pesquisa paginada funciona com Skip = a partir de qual quer começar a listagem e '
                                'limit = até onde ir essa paginação.')
async def skip_limit(skip: int, limit: int):
    try:
        result_skip_limit = Service_Trainer.skip_limit_trainers(collection_db, skip, limit)
        return result_skip_limit
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Certifique que o número de Skip ou Limit é válido...")


@router_trainer.post('/Created_Trainers',
                     name='Criação de Treinador',
                     description= 'Definir métricas para criação do treinador no banco de dados.')
async def create_user(user:Model_Create):
    try:
        insert = RepositoryMongo.insert_object(collection_db, dict(user))
        return ('User created')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Verifique se os tipos de dados de criação estão de acordo...")


@router_trainer.put('/Update_Trainers',
                    name="Update de Treinadores",
                    description= 'Definir métricas para alteração em treinador já existente no Banco de dados.')
async def update_trainers(user: Model_Up, unique_id: str):
    try:
        update = Service_Trainer.update_trainers(collection_db, unique_id, user)
        return (f'Update{update} Sucess')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Verifique se os dados passados para update são válidos.")


@router_trainer.delete('/Delete_Trainer',
                       name="Deletar Treinador",
                       description='Utilizar o "Unique_id" para apagar o treinador do Banco de dados.')
async def delete_trainers(unique_id: str):
    try:
        Service_Trainer.delete_trainers(collection_db,unique_id)
        return ('Sucess! Trainer Delete')
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Verifique novamente se o ID informado está correto..."
        )


@router_trainer.put('/soft_delete',
                    name="Soft Delete",
                    description="O soft delete altera o status do treinador para False, retirando da lista de paginação.")
async def soft_delete(soft: Soft, unique_id: str):
    try:
        soft_delete = Service_Trainer.soft_delete(collection_db, unique_id, soft)
        return (f'{soft_delete} Altered.')
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Verifique novamente o Unique_id informado."
        )



