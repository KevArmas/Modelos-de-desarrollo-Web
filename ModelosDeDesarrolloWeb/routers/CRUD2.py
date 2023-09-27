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
    Peliculas(id=12, Titulo= "The Departed", Genero="Crime" , Año=2006, Director= "Martin Scorsese" , Oscares= 4), 
    Peliculas(id=13, Titulo= "The Godfather Part II", Genero="Crime" , Año=1974, Director= "Francis Ford Coppola" , Oscares= 6), 
    Peliculas(id=14, Titulo= "The Good, the Bad and the Ugly", Genero="Western" , Año=1966, Director= "Sergio Leone" , Oscares= 1), 
    Peliculas(id=15, Titulo= "Whiplash", Genero="Drama" , Año=2014, Director= "Damien Chazelle" , Oscares= 3), 
    Peliculas(id=16, Titulo= "Parasite", Genero="Comedy" , Año=2019, Director= "Bong Joon-ho" , Oscares= 4), 
    Peliculas(id=17, Titulo= "Roma", Genero="Drama" , Año=2018, Director= "Alfonso Cuarón" , Oscares= 3), 
    Peliculas(id=18, Titulo= "The Shape of Water", Genero="Drama" , Año=2017, Director= "Guillermo del Toro" , Oscares= 4), 
    Peliculas(id=19, Titulo= "1917", Genero="War" , Año=2019, Director= "Sam Mendes" , Oscares= 3), 
    Peliculas(id=20, Titulo= "Moonlight", Genero="Drama" , Año=2016, Director= "Barry Jenkins" , Oscares= 3) ]

#***Get
@router.get("/peliculasclass2/")
async def peliculasclass():
    return (peliculas_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/


#***Get con Filtro Path
@router.get("/peliculasclass2/{id}")
async def peliculasclass(id:int):
    peliculass=filter (lambda peliculas: peliculas.id == id, peliculas_list)  #Función de orden superior
    try:
        return list(peliculass)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/1


#***Get con Filtro Query
@router.get("/peliculasclass2/")
async def get_peliculas(id: int):
    for peliculas in peliculas_list:
        if peliculas.id == id:
            return peliculas
    raise HTTPException(status_code=404, detail="peliculas not found")

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@router.post("/peliculasclass2/", response_model=Peliculas, status_code=status.HTTP_201_CREATED) #Añadir primer codigo de error correspondiente al metodo usando (Si es POST entonces usar POST)
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
@router.put("/peliculasclass2/", response_model=Peliculas, status_code=status.HTTP_201_CREATED)
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
@router.delete("/peliculasclass2/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_peliculas(id: int):
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == id:
            del peliculas_list[index]  # Remove the peliculas from the list
            return  # No need to return anything, just use 204 status code

    # If the loop completes without finding the peliculas, can raise a 404 error.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The peliculas you're trying to delete does not exist")

    #http://127.0.0.1:8000/peliculasclass/1


