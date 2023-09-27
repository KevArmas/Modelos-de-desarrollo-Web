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
    Peliculas(id=57, Titulo= "Lord of the Rings: The Return of the King", Genero="Adventure" , Año=2003, Director= "Peter Jackson" , Oscares= 11), 
    Peliculas(id=58, Titulo= "The Aviator", Genero="Biography" , Año=2004, Director= "Martin Scorsese" , Oscares= 5), 
    Peliculas(id=59, Titulo= "Million Dollar Baby", Genero="Drama" , Año=2004, Director= "Clint Eastwood" , Oscares= 4), 
    Peliculas(id=60, Titulo= "Crash", Genero="Drama" , Año=2005, Director= "Paul Haggis" , Oscares= 3), 
    Peliculas(id=61, Titulo= "Brokeback Mountain", Genero="Drama" , Año=2005, Director= "Ang Lee" , Oscares= 3), 
    Peliculas(id=62, Titulo= "Babel", Genero="Drama" , Año=2006, Director= "Alejandro González Iñárritu" , Oscares= 2), 
    Peliculas(id=63, Titulo= "The Departed", Genero="Crime" , Año=2006, Director= "Martin Scorsese" , Oscares= 4), 
    Peliculas(id=64, Titulo= "No Country for Old Men", Genero="Crime" , Año=2007, Director= "Joel Coen, Ethan Coen" , Oscares= 4), 
    Peliculas(id=65, Titulo= "Slumdog Millionaire", Genero="Drama" , Año=2008, Director= "Danny Boyle" , Oscares= 8) ]

#***Get
@router.get("/peliculasclass7/")
async def peliculasclass():
    return (peliculas_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/


#***Get con Filtro Path
@router.get("/peliculasclass7/{id}")
async def peliculasclass(id:int):
    peliculass=filter (lambda peliculas: peliculas.id == id, peliculas_list)  #Función de orden superior
    try:
        return list(peliculass)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/1


#***Get con Filtro Query
@router.get("/peliculasclass7/")
async def get_peliculas(id: int):
    for peliculas in peliculas_list:
        if peliculas.id == id:
            return peliculas
    raise HTTPException(status_code=404, detail="peliculas not found")

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@router.post("/peliculasclass7/", response_model=Peliculas, status_code=status.HTTP_201_CREATED) #Añadir primer codigo de error correspondiente al metodo usando (Si es POST entonces usar POST)
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
@router.put("/peliculasclass7/", response_model=Peliculas, status_code=status.HTTP_201_CREATED)
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
@router.delete("/peliculasclass7/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_peliculas(id: int):
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == id:
            del peliculas_list[index]  # Remove the peliculas from the list
            return  # No need to return anything, just use 204 status code

    # If the loop completes without finding the peliculas, can raise a 404 error.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The peliculas you're trying to delete does not exist")

    #http://127.0.0.1:8000/peliculasclass/1


