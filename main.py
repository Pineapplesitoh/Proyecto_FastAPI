from fastapi import FastAPI
from database import database as connection
from database import User
from schemas import UserRequestModel
from fastapi import HTTPException

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

@app.post('/users')
async def create_user(user_request: UserRequestModel):
    user = User.create(
        username = user.username,
        email = user.email
    )
    return user_request

@app.get('/users/{user_id}')
async def get_user(user_id):
    user = User.select().where(User.id == user.id).first()

    if user:
        return True
    else:
        return HTTPException(404, 'User not found')
