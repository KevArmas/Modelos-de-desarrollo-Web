from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Passanger(BaseModel):
    Pid: int
    Name:str
    Pclass: int
    Survived: bool
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Embarked: str


passanger_list=[
    Passanger(Pid= 1, Name= "Braund, Mr. Owen Harris", Pclass= 3 , Survived= 0, Sex= "male" , Age= 22, SibSp= 1 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 2, Name= "Cumings, Mrs. John Bradley (Florence Briggs Thayer)", Pclass= 1 , Survived= 1, Sex= "female" , Age= 38, SibSp= 1 , Parch= 0, Embarked= "C"), 
    Passanger(Pid= 3, Name= "Heikkinen, Miss. Laina", Pclass= 3 , Survived= 1, Sex= "female" , Age= 26, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 4, Name= "Futrelle, Mrs. Jacques Heath (Lily May Peel)", Pclass= 1 , Survived= 1, Sex= "female" , Age= 35, SibSp= 1 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 5, Name= "Allen, Mr. William Henry", Pclass= 3 , Survived= 0, Sex= "male" , Age= 35, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 6, Name= "Moran, Mr. James", Pclass= 3 , Survived= 0, Sex= "male" , Age= 21, SibSp= 0 , Parch= 0, Embarked= "Q"), 
    Passanger(Pid= 7, Name= "McCarthy, Mr. Timothy J", Pclass= 1 , Survived= 0, Sex= "male" , Age= 54, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 8, Name= "Palsson, Master. Gosta Leonard", Pclass= 3 , Survived= 0, Sex= "male" , Age= 2, SibSp= 3 , Parch= 1, Embarked= "S"), 
    Passanger(Pid= 9, Name= "Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)", Pclass= 3 , Survived= 1, Sex= "female" , Age= 27, SibSp= 0 , Parch= 2, Embarked= "S"), 
    Passanger(Pid= 10, Name= "Nasser, Mrs. Nicholas (Adele Achem)", Pclass= 2 , Survived= 1, Sex= "female" , Age= 14, SibSp= 1 , Parch= 0, Embarked= "C"), 
    Passanger(Pid= 11, Name= "Sandstrom, Miss. Marguerite Rut", Pclass= 3 , Survived= 1, Sex= "female" , Age= 4, SibSp= 1 , Parch= 1, Embarked= "S"), 
    Passanger(Pid= 12, Name= "Bonnell, Miss. Elizabeth", Pclass= 1 , Survived= 1, Sex= "female" , Age= 58, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 13, Name= "Saundercock, Mr. William Henry", Pclass= 3 , Survived= 0, Sex= "male" , Age= 20, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 14, Name= "Andersson, Mr. Anders Johan", Pclass= 3 , Survived= 0, Sex= "male" , Age= 39, SibSp= 1 , Parch= 5, Embarked= "S"), 
    Passanger(Pid= 15, Name= "Vestrom, Miss. Hulda Amanda Adolfina", Pclass= 3 , Survived= 0, Sex= "female" , Age= 14, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 16, Name= "Hewlett, Mrs. (Mary D Kingcome) ", Pclass= 2 , Survived= 1, Sex= "female" , Age= 55, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 17, Name= "Rice, Master. Eugene", Pclass= 3 , Survived= 0, Sex= "male" , Age= 2, SibSp= 4 , Parch= 1, Embarked= "Q"), 
    Passanger(Pid= 18, Name= "Williams, Mr. Charles Eugene", Pclass= 2 , Survived= 1, Sex= "male" , Age= 44, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 19, Name= "Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Pclass= 3 , Survived= 0, Sex= "female" , Age= 31, SibSp= 1 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 20, Name= "Masselmani, Mrs. Fatima", Pclass= 3 , Survived= 1, Sex= "female" , Age= 16, SibSp= 0 , Parch= 0, Embarked= "C"), 
    Passanger(Pid= 21, Name= "Fynney, Mr. Joseph J", Pclass= 2 , Survived= 0, Sex= "male" , Age= 35, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 22, Name= "Beesley, Mr. Lawrence", Pclass= 2 , Survived= 1, Sex= "male" , Age= 34, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 23, Name= "McGowan, Miss. Anna 'Annie'", Pclass= 3 , Survived= 1, Sex= "female" , Age= 15, SibSp= 0 , Parch= 0, Embarked= "Q"), 
    Passanger(Pid= 24, Name= "Sloper, Mr. William Thompson", Pclass= 1 , Survived= 1, Sex= "male" , Age= 28, SibSp= 0 , Parch= 0, Embarked= "S"), 
    Passanger(Pid= 25, Name= "Palsson, Miss. Torborg Danira", Pclass= 3 , Survived= 0, Sex= "female" , Age= 8, SibSp= 3 , Parch= 1, Embarked= "S"), 
    Passanger(Pid= 26, Name= "Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)", Pclass= 3 , Survived= 1, Sex= "female" , Age= 38, SibSp= 1 , Parch= 5, Embarked= "S") 
]

#***Get
@app.get("/passangersclass/")
async def passangersclass():
    return (passanger_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/passangerclass/


#***Get con Filtro Path
@app.get("/passangersclass/{Pid}")
async def passangersclass(Pid:int):
    passangers=filter (lambda passanger: passanger.Pid == Pid, passanger_list)  #Función de orden superior
    try:
        return list(passangers)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/passangersclass/1


#***Get con Filtro Query
@app.get("/usersclass/")
async def get_passenger(Pid: int):
    for passenger in passanger_list:
        if passenger.Pid == Pid:
            return passenger
    raise HTTPException(status_code=404, detail="Passenger not found")

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@app.post("/passangersclass/", response_model=Passanger, status_code=status.HTTP_201_CREATED) #Añadir primer codigo de error correspondiente al metodo usando (Si es POST entonces usar POST)
async def passangersclass(passanger:Passanger):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_passanger in enumerate(passanger_list):
        if saved_passanger.Pid == passanger.Pid:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el usuario ya existe")  #Cambiar info que aparece asi como tambien el status (Revisar que informacion es diferente de arriba y abajo y por que )
    else:
        passanger_list.append(passanger)
        return passanger
    
    #http://127.0.0.1:8000/passangerclass/
   
   
    #***Put
@app.put("/passangersclass/", response_model=Passanger, status_code=status.HTTP_201_CREATED)
async def passangersclass(passanger:Passanger):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_passanger in enumerate(passanger_list):
        if saved_passanger.Pid == passanger.Pid:  #Checks if the saved Pid is the same as the one requested
           raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="The user doesn't exist")

    else:
        passanger_list.append(passanger)
        return passanger
    
    #http://127.0.0.1:8000/passangersclass/
    
    
        #***Delete
@app.delete("/passangersclass/{Pid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_passanger(Pid: int):
    for index, saved_passanger in enumerate(passanger_list):
        if saved_passanger.Pid == Pid:
            del passanger_list[index]  # Remove the passanger from the list
            return  # No need to return anything, just use 204 status code

    # If the loop completes without finding the passanger, can raise a 404 error.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The passanger you're trying to delete does not exist")

    #http://127.0.0.1:8000/passangersclass/1


