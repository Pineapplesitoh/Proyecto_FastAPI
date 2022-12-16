from fastapi import FastAPI
from database import MySQLDatabase

app = FastAPI(title='Proyecto_FastAPI',
              description='Proyecto realizado en python',
              version='1.0.1')

@app.get('/')
async def index():
    return "Hola Mundo"

@app.get('/about')
async def about():
    return 'Estamos en el about'
