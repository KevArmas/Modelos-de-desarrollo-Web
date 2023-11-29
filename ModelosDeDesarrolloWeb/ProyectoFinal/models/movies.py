from pydantic import BaseModel

class Peliculas(BaseModel):
    id: int | None
    Titulo: str
    Genero: str
    Año: int
    Director: str
    Oscares: int

class Peliculas1(BaseModel):
    id: int | None
    Titulo: str
    Genero: str
    Año: int
    Director: str
    Oscares: int