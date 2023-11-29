#Este fichero será encargado de gestionar la conexión de nuestra base de datos con Mongo DB
import pymongo
from pymongo import MongoClient

#Instancia de tipo MongoClient (si no se le asignan argumentos se conecta al localhost por default)
#db_client= MongoClient()

MONGO_TIEMPO_FUERA = 1000
# Replace the MONGO_URL assignment with your actual MongoDB connection string
MONGO_URL = "mongodb+srv://kevarmashernandez:61JJhPeB6A5khz4m@modelosweb.3jke5d8.mongodb.net/?retryWrites=true&w=majority"

try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Conexion a MongoDB exitosa")
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido" + str(errorTiempo))
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse" + str(errorConexion))
