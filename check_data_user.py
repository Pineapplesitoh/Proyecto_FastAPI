from database import DAO
from werkzeug.security import check_password_hash

dao = DAO()

def same_category(category_database, category_form):
    validate = False
    if (category_form == category_database):
        validate = True
    return validate

def verificar_usuario(Email, Contraseña):
    filter_user = dao.authentication_user(Email)
    if filter_user:
        same_passw = check_password_hash(filter_user[6], Contraseña)
        if same_passw==True:
            return filter_user
    return None

def verificar_pyme(Email, Contraseña):
    filter_user = dao.authentication_pyme(Email)
    if filter_user:
        same_passw = check_password_hash(filter_user[5], Contraseña)
        if same_passw==True:
            return filter_user
    return None

