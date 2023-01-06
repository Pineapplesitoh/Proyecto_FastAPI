from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import DAO
from check_data_user import verificar_usuario, verificar_pyme
from werkzeug.security import generate_password_hash

app = FastAPI(title="Proyecto Framework fastAPI",
              description="Proyecto para el ramo 'FLP'",
              version="1.0.1")

dao = DAO()

template = Jinja2Templates(directory="./GUI")


@app.get("/", response_class=HTMLResponse)  # Index
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})


@app.post("/", response_class=HTMLResponse)  # Index
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})


@app.get("/signin", response_class=HTMLResponse)  # Login
def signin(req: Request):
    return template.TemplateResponse("signin.html", {"request": req})


@app.post("/signin", response_class=HTMLResponse)  # Login
def signin(req: Request):
    return template.TemplateResponse("signin.html", {"request": req})


@app.get("/user", response_class=HTMLResponse)  # IU
def interface_user(req: Request):
    return template.TemplateResponse("user.php", {"request": req})


@app.post("/user", response_class=HTMLResponse)  # IU
def interface_user(req: Request):
    return template.TemplateResponse("user.php", {"request": req})


@app.get("/user_pyme", response_class=HTMLResponse)  # IU
def interface_user(req: Request):
    return template.TemplateResponse("user_pyme.html", {"request": req})

@app.post("/user_pyme", response_class=HTMLResponse)  # IU
def interface_user(req: Request):
    return template.TemplateResponse("user_pyme.html", {"request": req})


@app.post("/authentication_user")
async def authentication_user(req: Request, Email: str = Form(), Contraseña: str = Form()):
    verify = verificar_usuario(Email, Contraseña)
    a= dao.mostrar_publicaciones()
    if verify:
        return template.TemplateResponse("user.html", {"request": req, "data_user": verify, "publicaciones": a})
    else:
        return RedirectResponse("/user")

@app.post("/authentication_pyme")
async def authentication_pyme(req: Request, Email: str = Form(), Contraseña: str = Form()):
    verify = verificar_pyme(Email, Contraseña)
    if verify:
        return template.TemplateResponse("user_pyme.html", {"request": req, "data_pyme": verify})
    else:
        return RedirectResponse("/user_pyme")

@app.get("/signup", response_class=HTMLResponse)  # Registro de nuevo Usuario
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})


@app.post("/signup", response_class=HTMLResponse)  # Registro de nuevo Usuario
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

# Registro de nuevo Usuario
@app.get("/signup_pyme", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup_pyme.html", {"request": req})


# Registro de nuevo Usuario
@app.post("/signup_pyme", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup_pyme.html", {"request": req})


# Registro de nuevo Usuario
@app.get("/signin_pyme", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signin_pyme.html", {"request": req})

@app.post("/insertar_publicacion")
async def data_publicacion(Productos: str = Form(), Lugar: str = Form(), Precio: str = Form()):
    data_publicacion = [Productos,Lugar,Precio]
    dao.insert_new_publicacion(data_publicacion)
    return RedirectResponse("/")

@app.get("/mostrar_publicaciones", response_class=HTMLResponse) 
def mostrar_publicaciones():
    rows=  mostrar_publicaciones()
    return template.TemplateResponse("tables.html", rows = rows)

# Registro de nuevo Usuario
@app.post("/signin_pyme", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signin_pyme.html", {"request": req})


@app.post("/data_users")
async def data_users(RUT: str = Form(), Nombre: str = Form(), Apellidos: str = Form(),
                     Fecha_nacimiento: str = Form(), Telefono: str = Form(), Email: str = Form(),
                     Contraseña: str = Form()):
    data_user = [RUT, Nombre, Apellidos, Fecha_nacimiento,
                 Telefono, Email+"@estudiantesunap.cl", generate_password_hash(Contraseña)]
    dao.insert_new_User(data_user)
    return RedirectResponse("/signin")


@app.post("/data_pyme")
async def data_pyme(Nombre: str = Form(), Categoria: str = Form(), Telefono: str = Form(), Email: str = Form(),
                    Contraseña: str = Form()):
    data_pyme = [Nombre, Categoria, Telefono, Email, generate_password_hash(Contraseña)]
    dao.insert_new_PYME(data_pyme)
    return RedirectResponse("/signin_pyme")


@app.get("/contact", response_class=HTMLResponse)  # contacto
def contact(req: Request):
    return template.TemplateResponse("contact.html", {"request": req})
