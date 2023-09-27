from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class Peliculas(BaseModel):
    id: int
    Titulo: str
    Genero: str
    Año: int
    Director: str
    Oscares: int


peliculas_list=[ 
    Peliculas(id=1, Titulo= "The Shawshank Redemption", Genero="Drama" , Año=1994, Director= "Frank Darabont" , Oscares= 0), 
    Peliculas(id=2, Titulo= "The Godfather", Genero="Crime" , Año=1972, Director= "Francis Ford Coppola" , Oscares= 7), 
    Peliculas(id=3, Titulo= "The Dark Knight", Genero="Action" , Año=2008, Director= "Christopher Nolan" , Oscares= 2), 
    Peliculas(id=4, Titulo= "Schindler's List", Genero="Drama" , Año=1993, Director= "Steven Spielberg" , Oscares= 7), 
    Peliculas(id=5, Titulo= "Pulp Fiction", Genero="Crime" , Año=1994, Director= "Quentin Tarantino" , Oscares= 2), 
    Peliculas(id=6, Titulo= "12 Angry Men", Genero="Drama" , Año=1957, Director= "Sidney Lumet" , Oscares= 3), 
    Peliculas(id=7, Titulo= "The Lord of the Rings: The Return of the King", Genero="Adventure" , Año=2003, Director= "Peter Jackson" , Oscares= 11), 
    Peliculas(id=8, Titulo= "The Silence of the Lambs", Genero="Crime" , Año=1991, Director= "Jonathan Demme" , Oscares= 5), 
    Peliculas(id=9, Titulo= "Forrest Gump", Genero="Drama" , Año=1994, Director= "Robert Zemeckis" , Oscares= 6), 
    Peliculas(id=10, Titulo= "Titanic", Genero="Drama" , Año=1997, Director= "James Cameron" , Oscares= 11), 
    Peliculas(id=11, Titulo= "Inception", Genero="Action" , Año=2010, Director= "Christopher Nolan" , Oscares= 4) ]

#***Get
@router.get("/peliculasclass1/")
async def peliculasclass():
    return (peliculas_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/


#***Get con Filtro Path
@router.get("/peliculasclass1/{id}")
async def peliculasclass(id:int):
    peliculass=filter (lambda peliculas: peliculas.id == id, peliculas_list)  #Función de orden superior
    try:
        return list(peliculass)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/1


#***Get con Filtro Query
@router.get("/peliculasclass1/")
async def get_peliculas(id: int):
    for peliculas in peliculas_list:
        if peliculas.id == id:
            return peliculas
    raise HTTPException(status_code=404, detail="peliculas not found")

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@router.post("/peliculasclass1/", response_model=Peliculas, status_code=status.HTTP_201_CREATED) #Añadir primer codigo de error correspondiente al metodo usando (Si es POST entonces usar POST)
async def peliculasclass(peliculas:Peliculas):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el usuario ya existe")  #Cambiar info que aparece asi como tambien el status (Revisar que informacion es diferente de arriba y abajo y por que )
    else:
        peliculas_list.append(peliculas)
        return peliculas
    
    #http://127.0.0.1:8000/peliculasclass/
   
   
    #***Put
@router.put("/peliculasclass1/", response_model=Peliculas, status_code=status.HTTP_201_CREATED)
async def peliculasclass(peliculas:Peliculas):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == peliculas.id:  #Checks if the saved id is the same as the one requested
           raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="The user doesn't exist")

    else:
        peliculas_list.append(peliculas)
        return peliculas
    
    #http://127.0.0.1:8000/peliculasclass/
    
    
        #***Delete
@router.delete("/peliculasclass1/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_peliculas(id: int):
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == id:
            del peliculas_list[index]  # Remove the peliculas from the list
            return  # No need to return anything, just use 204 status code

    # If the loop completes without finding the peliculas, can raise a 404 error.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The peliculas you're trying to delete does not exist")

    #http://127.0.0.1:8000/peliculasclass/1


