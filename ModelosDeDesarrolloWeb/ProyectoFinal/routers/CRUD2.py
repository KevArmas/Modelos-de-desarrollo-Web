from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from bson import ObjectId
from jose import jwt, JWTError
import pymongo

from models.movies import Peliculas,Peliculas1
from connection import cliente

router = APIRouter()

database = cliente["Movies"]
collection = database["movies"]

router = APIRouter()

# Mostrar todos los objetos de mi bd
@router.get("/movies/get/", status_code=status.HTTP_202_ACCEPTED, response_description="success")
async def mostrar():
    resultados = []
    cursor = collection.find({})  

    for documento in cursor:
        movie = Peliculas(**documento)
        resultados.append({
            "id": str(documento["_id"]),
            **movie.dict()
        })

    return resultados

@router.post("/movies/post/", response_description="Movie succesfully added")
async def post(movie: Peliculas1):

    documento = movie.dict()

    if not documento["id"] == None:
        if len(documento["id"]) < 24:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id must be a 24 lenght hex value")

    if collection.find_one({"_id": ObjectId(movie.id)}):
        raise HTTPException(status_code=400, detail="Movie already exists")
    
    documento["_id"]=ObjectId(movie.id)
    documento.pop("id")

    resultado = collection.insert_one(documento)
    documento.pop("_id")
    documento["_id"]=str(resultado.inserted_id)
    documento = {"_id": documento.pop("_id"), **documento}

    return {"message": "Movie successfully added","movie": documento}

#Funcion actualizar

@router.put("/movies/put/{movie_id}", status_code=status.HTTP_200_OK, response_description="Movie succesfully updated")
async def actualizar_movie(movie_id: str, new_movie: Peliculas):
    result = collection.update_one({"_id": ObjectId(movie_id)}, {"$set": new_movie.dict()})
    if result.modified_count == 1:
        return {"message": "movie updated"}
    else:
        raise HTTPException(status_code=404, detail="Movie not found, no changes where made")

@router.delete("/movies/delete/{id}", status_code=status.HTTP_200_OK, response_description="movie succesfully deleted")
async def delete(id: str):
    eliminar_us = collection.delete_one({"_id": ObjectId(id)})
    if eliminar_us.deleted_count == 1:
        return {"message": "Movie deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")


'''
{
    "id": null,
    "CPU": "Intel",
    "RAM": "8GB",
    "Almacenamiento": "256GB",
    "Marca": "HP",
    "SO": "Windows"
}
'''