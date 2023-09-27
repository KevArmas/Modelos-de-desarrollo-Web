from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

router = FastAPI()

class Peliculas(BaseModel):
    id: int
    Titulo: str
    Genero: str
    Año: int
    Director: str
    Oscares: int


peliculas_list=[ 
    Peliculas(id=21, Titulo= "The King's Speech", Genero="Drama" , Año=2010, Director= "Tom Hooper" , Oscares= 4), 
    Peliculas(id=22, Titulo= "Argo", Genero="Thriller" , Año=2012, Director= "Ben Affleck" , Oscares= 3), 
    Peliculas(id=23, Titulo= "No Country for Old Men", Genero="Thriller" , Año=2007, Director= "Joel Coen, Ethan Coen" , Oscares= 4), 
    Peliculas(id=24, Titulo= "Slumdog Millionaire", Genero="Drama" , Año=2008, Director= "Danny Boyle" , Oscares= 8), 
    Peliculas(id=25, Titulo= "The Hurt Locker", Genero="War" , Año=2008, Director= "Kathryn Bigelow" , Oscares= 6), 
    Peliculas(id=26, Titulo= "Birdman or (The Unexpected Virtue of Ignorance)", Genero="Comedy" , Año=2014, Director= "Alejandro González Iñárritu" , Oscares= 4), 
    Peliculas(id=27, Titulo= "The Artist", Genero="Comedy" , Año=2011, Director= "Michel Hazanavicius" , Oscares= 5), 
    Peliculas(id=28, Titulo= "Spotlight", Genero="Drama" , Año=2015, Director= "Tom McCarthy" , Oscares= 2) ]

#***Get
@router.get("/peliculasclass/")
async def peliculasclass():
    return (peliculas_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/


#***Get con Filtro Path
@router.get("/peliculasclass/{id}")
async def peliculasclass(id:int):
    peliculass=filter (lambda peliculas: peliculas.id == id, peliculas_list)  #Función de orden superior
    try:
        return list(peliculass)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/1


#***Get con Filtro Query
@router.get("/peliculasclass/")
async def get_peliculas(id: int):
    for peliculas in peliculas_list:
        if peliculas.id == id:
            return peliculas
    raise HTTPException(status_code=404, detail="peliculas not found")

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@router.post("/peliculasclass/", response_model=Peliculas, status_code=status.HTTP_201_CREATED) #Añadir primer codigo de error correspondiente al metodo usando (Si es POST entonces usar POST)
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
@router.put("/peliculasclass/", response_model=Peliculas, status_code=status.HTTP_201_CREATED)
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
@router.delete("/peliculasclass/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_peliculas(id: int):
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == id:
            del peliculas_list[index]  # Remove the peliculas from the list
            return  # No need to return anything, just use 204 status code

    # If the loop completes without finding the peliculas, can raise a 404 error.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The peliculas you're trying to delete does not exist")

    #http://127.0.0.1:8000/peliculasclass/1


