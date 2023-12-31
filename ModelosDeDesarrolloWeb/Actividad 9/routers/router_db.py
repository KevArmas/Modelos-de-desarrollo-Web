from fastapi import APIRouter, HTTPException, status
from models.User import User
from schemas.user_schema import user_schema
from db.connection import db_client
from bson import ObjectId

router = APIRouter()


# ***Get
@router.get("/userdb/")
async def get_users():
    # Fetch all users from the MongoDB collection
    users = list(db_client.Computacion.users.find())

    # Convert MongoDB documents to User objects using the schema
    users_with_schema = [user_schema(user) for user in users]

    return users_with_schema

@router.get("/userdb/{username}")
async def get_users(username:str):
    try:
        new_user = user_schema(db_client.Computacion.users.find_one({"username":username}))
        return User(**new_user)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
# ***Post
@router.post("/userdb/")
async def usersclass(user: User):
    user_dict = dict (user) #convertir de User a JSON
    del user_dict["id"] #eliminar id
    id = db_client.Computacion.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.Computacion.users.find_one({"_id":id}))
    return User(**new_user)

# ***Put
@router.put("/userdb/{username}", response_model=User)
async def usersclass(user: User, username:str):
    newusername = user.username
    full_name = user.full_name
    email = user.email
    phone = user.phone

    filtro = {"username":username}
    newvalues = {"$set":{"full_name":full_name,
                         "email":email,
                         "phone":phone,
                         "username":newusername}}

    try:
        db_client.Computacion.users.update_one(filtro,newvalues)
        new_user = user_schema(db_client.Computacion.users.find_one({"username":newusername}))
        return User(**new_user)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

# ***Delete
@router.delete("/userdb/{username}")
async def delete_user(username: str):
    result = db_client.Computacion.users.delete_one({"username": username})

    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    return {"Usuario eliminado"}


