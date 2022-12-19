from peewee import *
import mysql.connector
from mysql.connector import Error

class DAO():
    
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
            host='localhost',
            port= 3306,
            user='root',
            password='Xcarpwesdiwem1',
            db='fastapi'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
    
    def registro_usuario(self,User):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSTER INTO users(Nombre,Apellido_p,Apellido_m,"
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))