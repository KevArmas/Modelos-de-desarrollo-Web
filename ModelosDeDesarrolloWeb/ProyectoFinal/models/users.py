from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    username:str
    full_name:str
    email:str
    phone:int
    password:str

class UserN(User):
    _id: ObjectId | None
    disabled: str

class UserN1(User):
    id: str | None
    disabled: str

class UserA(User):
    disabled:bool    