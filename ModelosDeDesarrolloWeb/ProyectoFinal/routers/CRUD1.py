from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import pymongo
from bson import ObjectId

from connection import cliente
from models.users import User,UserN,UserN1,UserA

router = APIRouter()

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION=1
SECRET="123456789"

router.mount("/static", StaticFiles(directory="static"), name="static")
oauth2=OAuth2PasswordBearer(tokenUrl="login")
crypt= CryptContext(schemes="bcrypt")

#Preguntar a Vicente que pedo con esto 
database = cliente["Alumnos"]
collection = database["users_db"]



#Showing the whole users DB through a get method
@router.get("/users/get/", status_code=status.HTTP_202_ACCEPTED, response_description="successfully charge")
async def show():
    users_list = []
    cursor = collection.find({})  #Cursor helps to move into the DB

    for users_db in cursor:
        user = UserN(* users_db)
        users_list.append({
            "id": str (users_db["_id"]),
            **user.dict()
        })

    return users_list

# Add Function using post method
@router.post("/users/post/", status_code=status.HTTP_201_CREATED, response_description="User succesfully added")
async def ad(user: UserN1):

 users_db = user.dict()
    if not users_db["id"] == None:
        if len (users_db["id"]) < 24:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id must be a 24 lenght hex value")

    # Check if user already exists 
    if collection.find_one({"_id": ObjectId(user.id)}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
 users_db["_id"]=ObjectId(user.id)
 users_db.pop("id")
 users_db["password"]=crypt.hash(user.password)

    Collection = collection.insert_one(users_db)
 users_db.pop("_id")
 users_db["_id"]=str(Collection.inserted_id)
 users_db = {"_id": users_db.pop("_id"), * users_db}

    return {"Message": "User has been added succesfully","User": users_db}


#Update Function with put method
@router.put("/users/put/{id}", status_code=status.HTTP_200_OK, response_description="User successfully updated")
async def update(id: str, user: User):
    update_user = collection.update_one({"_id": ObjectId(id)}, {"$set": user.dict()})
    if update_user.modified_count == 1:
        collection.update_one({"_id": ObjectId(id)}, {"$set": {"password": crypt.hash(user.password)}})
        return {"message": "User has been sucessfully updated"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found, no changes where made")

#Delete function using delete method
@router.delete("/users/delete/{id}", status_code=status.HTTP_200_OK, response_description="User deleted")
async def eliminar(id: str):
    pop_user = collection.delete_one({"_id": ObjectId(id)})
    if pop_user.deleted_count == 1:
        return {"message": "User succesfully deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


def search_user_db(username: str):
    users_db = list(collection.find({"username": username}))
    if any(user["username"] == username for user in users_db):
        return UserA(**users_db[0])


def search_user(username:str):
    users_db = collection.find({"username": username})
    if username in users_db:
        return UserA(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")

    return search_user_db(username)

async def current_user(user_db: UserA = Depends(auth_user)):
    if user_db.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user_db


@router.post("/login/")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = search_user_db(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire = datetime.utcnow() + access_token_expiration
    access_token = {"sub": user_db.username, "exp": expire}
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me/")
async def me(user_db:UserA= Depends (current_user)):
    imagen = f"static/{user_db.username}.png"
    return FileResponse (imagen)