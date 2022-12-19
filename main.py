from fastapi import FastAPI, HTTPException, Request, Form
from schemas import UserRequestModel, UserResponseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import DAO

templates = Jinja2Templates(directory="./GUI")

app = FastAPI(title='Proyecto_FastAPI',
              description='Proyecto realizado en python',
              version='1.0.1')

@app.get('/', response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse("cuerpo/index.html", {"request": req})
@app.post('/', response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse("cuerpo/index.html", {"request": req})
    
@app.get('/users', response_class=HTMLResponse)
async def create_user(user_request: UserRequestModel, req: Request):
    return user_request, templates.TemplateResponse("cuerpo/singup.html", {"request": req})
@app.post('/users', response_class=HTMLResponse)
async def create_user(Nombre: str = Form(), Apellido_p: str = Form(), Apellido_m: str = Form(), 
                      Fecha_Nacimiento: str = Form(),Run: str = Form(), Genero: str = Form(),
                      Telefono: str = Form(), Email: str = Form(), Contraseña: str = Form()
                      ):
    data_user = []
    dao.
    return templates.TemplateResponse("cuerpo/singup.html", {"request": req})