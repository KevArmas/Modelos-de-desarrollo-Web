# En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
# Invocamos la entidad que hemos creado ****new
from models.User import User
# Importamos la instancia que devolvera al usuario en formato user ***new
from schemas.user_schema import user_schema
# Importamos nuestro cliente para poder agregar usuarios a la db****new
from db.connection import db_client
from db import connection

# Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

# Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)
users_list = []

# ***Get
@router.get("/userdb/")
async def usersclass():
    users_list = []
    try:
        for userdb in connection.Computacion.users.find():
            userJSON = user_schema(userdb)
            users_list.append(User(**userJSON))
        return users_list
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/userdb/{username}")
async def usersclass(username:str):
    try:
        new_user = user_schema(connection.Computacion.users.find_one({"username":username}))
        return User(**new_user)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
# ***Post
@router.post("/userdb/")
async def usersclass(user: User):
    user_dict = dict (user) #convertir de User a JSON
    del user_dict["id"] #eliminar id
    id = connection.Computacion.users.insert_one(user_dict).inserted_id
    new_user = user_schema(connection.Computacion.users.find_one({"_id":id}))
    return User(**new_user)

# ***Put
@router.put("/userdb/{username}", response_model=User)
async def usersclass(user: User, username:str):
    newusername = user.username
    full_name = user.full_name
    email = user.email
    phone = user.phone
    disabled = user.disabled

    filtro = {"username":username}
    newvalues = {"$set":{"full_name":full_name,
                         "email":email,
                         "phone":phone,
                         "disabled":disabled,
                         "username":newusername}}

    try:
        connection.Computacion.users.update_one(filtro,newvalues)
        new_user = user_schema(connection.Computacion.users.find_one({"username":newusername}))
        return User(**new_user)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

# ***Delete
@router.delete("/userdb/{username}")
async def usersclass(username:str):

    try:
        connection.Computacion.users.delete_one({"username":username})
        return {"Usuario eliminado"}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


