from fastapi import FastAPI
from database import database as connection
from database import User

app = FastAPI(title='Proyecto_FastAPI',
              description='Proyecto realizado en python',
              version='1.0.1')

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        
    connection.create_tables([User])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.get('/')
async def index():
    return "Hola Mundo"

@app.get('/about')
async def about():
    return 'Estamos en el about'
