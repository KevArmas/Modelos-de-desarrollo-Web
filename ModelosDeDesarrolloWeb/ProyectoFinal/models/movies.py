from pydantic import BaseModel
from bson import ObjectId

class Peliculas(BaseModel):
    _id: ObjectId | None
    Titulo: str
    Genero: str
    Año: int
    Director: str
    Oscares: int

class Peliculas1(BaseModel):
    id: str | None
    Titulo: str
    Genero: str
    Año: int
    Director: str
    Oscares: int