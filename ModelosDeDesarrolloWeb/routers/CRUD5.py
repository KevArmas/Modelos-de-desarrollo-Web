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
     Peliculas(id=38, Titulo= "One Flew Over the Cuckoo's Nest", Genero="Drama" , Año=1975, Director= "Miloš Forman" , Oscares= 5), 
    Peliculas(id=39, Titulo= "Annie Hall", Genero="Comedy" , Año=1977, Director= "Woody Allen" , Oscares= 4), 
    Peliculas(id=40, Titulo= "Kramer vs. Kramer", Genero="Drama" , Año=1979, Director= "Robert Benton" , Oscares= 5), 
    Peliculas(id=41, Titulo= "Ordinary People", Genero="Drama" , Año=1980, Director= "Robert Redford" , Oscares= 2), 
    Peliculas(id=42, Titulo= "Terms of Endearment", Genero="Comedy" , Año=1983, Director= "James L. Brooks" , Oscares= 5), 
    Peliculas(id=43, Titulo= "Amadeus", Genero="Biography" , Año=1984, Director= "Miloš Forman" , Oscares= 8), 
    Peliculas(id=44, Titulo= "Platoon", Genero="War" , Año=1986, Director= "Oliver Stone" , Oscares= 4), 
    Peliculas(id=45, Titulo= "Rain Man", Genero="Drama" , Año=1988, Director= "Barry Levinson" , Oscares= 4), 
    Peliculas(id=46, Titulo= "Driving Miss Daisy", Genero="Comedy" , Año=1989, Director= "Bruce Beresford" , Oscares= 4), 
    Peliculas(id=47, Titulo= "Dances with Wolves", Genero="Western" , Año=1990, Director= "Kevin Costner" , Oscares= 7), 
    Peliculas(id=48, Titulo= "Unforgiven", Genero="Western" , Año=1992, Director= "Clint Eastwood" , Oscares= 4), 
    Peliculas(id=49, Titulo= "Braveheart", Genero="Drama" , Año=1995, Director= "Mel Gibson" , Oscares= 5), 
    Peliculas(id=50, Titulo= "The English Patient", Genero="Drama" , Año=1996, Director= "Anthony Minghella" , Oscares= 9), 
    Peliculas(id=51, Titulo= "Titanic", Genero="Drama" , Año=1997, Director= "James Cameron" , Oscares= 11) ]

#***Get
@router.get("/peliculasclass5/")
async def peliculasclass():
    return (peliculas_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/


#***Get con Filtro Path
@router.get("/peliculasclass5/{id}")
async def peliculasclass(id:int):
    peliculass=filter (lambda peliculas: peliculas.id == id, peliculas_list)  #Función de orden superior
    try:
        return list(peliculass)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/peliculasclass/1


#***Get con Filtro Query
@router.get("/peliculasclass5/")
async def get_peliculas(id: int):
    for peliculas in peliculas_list:
        if peliculas.id == id:
            return peliculas
    raise HTTPException(status_code=404, detail="peliculas not found")

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@router.post("/peliculasclass5/", response_model=Peliculas, status_code=status.HTTP_201_CREATED) #Añadir primer codigo de error correspondiente al metodo usando (Si es POST entonces usar POST)
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
@router.put("/peliculasclass5/", response_model=Peliculas, status_code=status.HTTP_201_CREATED)
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
@router.delete("/peliculasclass5/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_peliculas(id: int):
    for index, saved_peliculas in enumerate(peliculas_list):
        if saved_peliculas.id == id:
            del peliculas_list[index]  # Remove the peliculas from the list
            return  # No need to return anything, just use 204 status code

    # If the loop completes without finding the peliculas, can raise a 404 error.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The peliculas you're trying to delete does not exist")

    #http://127.0.0.1:8000/peliculasclass/1


