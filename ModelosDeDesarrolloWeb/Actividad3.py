#POST
from fastapi import FastAPI
app = FastAPI()
from pydantic import BaseModel

class Passanger(BaseModel):
    Pid: int
    Name:str
    Pclass: int
    Survived: bool
    Sex: str
    Age: int
    SibSp: bool
    Parch: int
    Embarked: str


Passanger_list=[0]

