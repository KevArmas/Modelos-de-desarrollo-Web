#Este fichero será encargado de gestionar la conexión de nuestra base de datos con Mongo DB
import pymongo
from pymongo import MongoClient

#Instancia de tipo MongoClient (si no se le asignan argumentos se conecta al localhost por default)
#db_client= MongoClient()

db_url = MongoClient("mongodb+srv://kevarmashernandez:61JJhPeB6A5khz4m@modelosweb.3jke5d8.mongodb.net/?retryWrites=true&w=majority").kevarmashernandez
time_out=1000

try:
    cliente=pymongo.MongoClient(db_url,serverSelectionTimeoutMS=time_out)
    cliente.server_info()
    print("Conexion a MongoDB exitosa")

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse"+errorConexion)