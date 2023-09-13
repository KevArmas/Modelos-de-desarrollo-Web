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
@app.get("/usersclass/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#***Get con Filtro Path
@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1


#***Get con Filtro Query
@app.get("/usersclass/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@app.post("/usersclass/", response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/
   
   
    #***Put
@app.put("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@app.delete("/usersclass/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    
    #http://127.0.0.1:8000/usersclass/1