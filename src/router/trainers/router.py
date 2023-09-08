from fastapi import APIRouter
from src.repository.repository import Repository
from src.services.trainers.services import Service
from src.domain.DTO.schema_docs_mongo import Model_Create, Model_Up, Soft

collection = "trainers"
trainer = APIRouter()


@trainer.get('/Get_trainers', name="Pesquisa de Treinadores",
                           description="Ao colocar o unique_id do treinador desejado, retornará os dados do mesmo.")
async def get_trainer(unique_id: str):
   find = Service.get_trainers(collection, unique_id)
   return find

@trainer.get('/skip_limit')
async def skip_limit(skip: int, limit: int):
    result = Service.skip_limit_trainers(collection, skip, limit)
    return result

@trainer.post('/Created_Trainers')
async def create_user(user:Model_Create):
    insert = Repository.insert_object(collection, dict(user))
    return ('User created')

@trainer.put('/')
async def update_trainers(user: Model_Up, unique_id: str):
    update = Service.update_trainers(collection, unique_id, user)
    return (f'Update{update} Sucess')

@trainer.delete('/')
async def delete_trainers(unique_id: str):
    delete = Service.delete_trainers(collection,unique_id)
    return ('Sucess!')

@trainer.put('/soft_delete')
async def soft_delete(soft: Soft, unique_id: str):
    soft = Service.soft_delete(collection, unique_id, soft)
    return (f'{soft} Altered.')



