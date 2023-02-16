from fastapi import FastAPI
from src.router.trainers.router import trainer
from src.router.pokemons.router import pokemon
from src.router.capture.router import capture


app = FastAPI(title= 'POKEMON BATTLE',
              description='Operação CRUD de trainers e pokemons,'
                            ' fazendo uso de API open source de pokemon para simular capturas e batalhas, '
                           'utilizando MONGODB para armazenamento.',
              version='0.0.1'
              )


app.include_router(trainer, tags=['Trainers'])
app.include_router(pokemon, tags=['Pokemons'])
app.include_router(capture, tags=['capture'])




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)