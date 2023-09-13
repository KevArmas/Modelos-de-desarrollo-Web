#POST
from fastapi import FastAPI
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
 #We use the following in the browser to access the class: http://127.0.0.1:8000/passangersclass/


#***Post
@app.post("/passangersclass/")
async def passangersclass(passanger:Passanger):
    
    found=False     #The flag is used to verify if the passanger exists 
    
    for index, saved_passanger in enumerate(passanger_list):
        if saved_passanger.Pid == passanger.Pid:  #If passanger's Id it's the same as an already registered passanger
            return {"error":"The passanger already exists"}
    else:
        passanger_list.append(passanger)
        return passanger
    
@app.put("/passangersclass/")
async def passangersclass(passanger:Passanger):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_passanger in enumerate(passanger_list):
        if saved_passanger.Pid == passanger.Pid:  #Checks if the saved Pid is the same as the one requested
           passanger_list[index] = passanger #If it exists it access to the list's index
           found=True
           
    if not found:
        return {"error":"The passanger has not been registered"}
    else:
        return passanger
    

@app.delete("/passangersclass/{Pid}")
async def passangersclass(Pid:int):
    
    found=False     #The flag is used to check if we've found the passanger 
    
    for index, saved_passanger in enumerate(passanger_list):
        if saved_passanger.Pid == Pid:  #Checks if the saved Pid is the same as the one requested
           del passanger_list[index]  #If exists then delete it 
           found=True
           return "Passanger has been deleted"
       
    if not found:
        return {"error":"The passanger has not been deleted"}