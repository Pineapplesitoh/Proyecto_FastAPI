import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'fastapi'
            )
        except Exception as exx:
            return ("ERROR al intentar la conexión: {0}".format(exx))

    def insert_new_User(self, data_user):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO users (RUT,Nombre,Apellidos,Fecha_nacimiento,Telefono,Email,Contraseña) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"
                cursor.execute(sql.format(data_user[0],data_user[1],data_user[2],data_user[3],data_user[4],data_user[5],data_user[6]))
                self.connection.commit()
            except Error as ex:
                return ("ERROR: {0}".format(ex))
            
    def insert_new_PYME(self, data_pyme):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO pyme (Nombre,Categoria,Telefono,Email,Contraseña) VALUES ('{0}','{1}','{2}','{3}','{4}')"
                cursor.execute(sql.format(data_pyme[0],data_pyme[1],data_pyme[2],data_pyme[3],data_pyme[4]))
                self.connection.commit()
            except Error as ex:
                return ("ERROR: {0}".format(ex))
            
    def insert_new_publicacion(self, data_publicacion):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO publicaciones (Productos,Lugar,Precio) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sql.format(data_publicacion[0],data_publicacion[1],data_publicacion[2]))
                self.connection.commit()
            except Error as ex:
                return ("ERROR: {0}".format(ex))

    def authentication_user(self, Email):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "SELECT * FROM users WHERE Email = '{}'"
                cursor.execute(sql.format(Email))
                return cursor.fetchone()
            except Error as ex:
                return ("ERROR: {0}".format(ex))
            
    def authentication_pyme(self, Email):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "SELECT * FROM pyme WHERE Email = '{}'"
                cursor.execute(sql.format(Email))
                return cursor.fetchone()
            except Error as ex:
                return ("ERROR: {0}".format(ex))
            
    def mostrar_publicaciones(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "SELECT * FROM publicaciones"
                cursor.execute(sql.format())
                rows = cursor.fetchall()
                return rows
            except Error as ex:
                return ("ERROR: {0}".format(ex))
    