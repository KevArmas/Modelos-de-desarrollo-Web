# Instalamos libreria de criptografía para encriptar token
# pip install "python-jose[cryptography]"

# Instalamos libreria que contiene el algoritmo de encriptación
# pip install "passlib[bcrypt]"

# Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, Depends, HTTPException, status
# Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel


from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi import Depends
import requests

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# Importamos librería jwt
from jose import jwt, JWTError
# Importamos libreria passlib (algoritmo de encriptación)
from passlib.context import CryptContext
# Importamos libreria de fechas para la expiración del token
from datetime import datetime, timedelta
# Importamos la clase staticfiles para recursos estáticos****
from fastapi.staticfiles import StaticFiles

# Implementamos algoritmo de haseo para encriptar contraseña
ALGORITHM = "HS256"
# Duración de autenticación
ACCESS_TOKEN_DURATION = 1
# Creamos un secret
SECRET = "123456789"

# Creamos un objeto o instancia a partir de la clase FastAPI
app = FastAPI()


# Creamos una app para acceder al directorio de recursos estaticos***
app.mount("/sources", StaticFiles(directory="sources"), name="sources")

# Autenticación por contraseña para eso:
# Creamos un endpoint llamado "login"
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Creamos contexto de encriptación para eso importamos libreria passlib y elegimos algoritmo de incriptación "bcrypt"
# Utilizamos bcrypt generator para encriptar nuestras contraseñas
crypt = CryptContext(schemes="bcrypt")

# generamos la contraseña encriptada para guardarla en base de datos
# https://bcrypt-generator.com/4


class User(BaseModel):
    username: str
    full_name: str
    email: str
    phone: str
    photo:str
    disabled: bool


class equipo(BaseModel):
    username: str
    disabled: bool
# Definimos la clase para el usuario de base de datos


class UserDB(User):
    password: str

users_db = {
    "Yosselin": {
        "username": "Yosselin",
        "full_name": "Yosselin Pablo Ruiz",
        "email": "yosselin.pablo@alumno.buap.mx",
        "phone":"2288358188",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$ytMkgWTSwq2eqSY5sq6wxuAeTPEbbsf1GIM6J4Skvcy/RuEFY6L5u"
    },
    "Abraham": {
        "username": "Abraham",
        "full_name": "Abraham Coagtle Temis",
        "email": "abraham.coagtle@alumno.buap.mx",
        "phone":"2731327748",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$ESROW9KIqlQMo9.P8UHaOuf7WJHRReM4oVDchcdusrwJthRXSbo2K"
    },
    "Victor": {
        "username": "Victor",
        "full_name": "Victor Manuel Rosales Zayas",
        "email": "victor.rosalesz@alumno.buap.mx",
        "phone":"2224415653",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$0JOD5t2xIQy/9AFCfILnIO5BB8x3.ldHdELwXzfki8x7rOYRibIRK"
    },
    "Juan": {
        "username": "Juan",
        "full_name": "Juan Pablo Mendoza Armas",
        "email": "juan.mendozaar@alumno.buap.mx ",
        "phone":"2281776285",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$gLJ9jwSn2KwSaU7W5jD2t.c81Ki7G6nLURJhAoMq9Gbd8whFAYAke"
    },
    "Kevin": {
        "username": "Kevin",
        "full_name": "Kevin Armas Hernandez",
        "email": "kevin.armas@alumno.buap.mx",
        "phone":"6141998990",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$VfNKay8J6pg5eFwvyzDT5OU74is8o9tgIn7xlmUWyrtZtGn3SNJhe",
    },
    "Luis": {
        "username": "Luis",
        "full_name": "Luis Delfino Castro Nava",
        "email": "luis.castron@alumno.buap.mx",
        "phone": "8110502639",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$2M4mAxp22IZnWU.V8g8IVuZC8KLhiKzl5RF1lC7CCDjW3H7T5H7um",
    },
    "Estefania": {
        "username": "Estefania",
        "full_name": "Estefania Rodríguez Martínez",
        "email": "estefania.rodriguezma@alumno.buap.mx ",
        "phone": "2228669227",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$Xgd2Op3mAjc7t1CJRb1wQeORiLTW/WTMzhIwpmKzbDI0U/48848pW",
    },
    "Pilar": {
        "username": "Pilar",
        "full_name": "Pilar Hernandez Zambrano",
        "email": "pilar.hernandezz@alumno.buap.mx",
        "phone": "2223223454",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$9MKzlxRdkulJT1wqns/Xy.q/C5F/lQ1iglyRjP72Ua6AQQB.bdXsq",
    },
    "Vicente": {
        "username": "Vicente",
        "full_name": "Vicente Zavaleta Sanchez",
        "email": "vicente.zavaletas@alumno.buap.mx",
        "phone": "2212671849",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$GaxxWCilDRL5OYXavoA0x.6YDjcetI.3dhWxRVxliuXlCD5rv41ru",
    },
    "Jose": {
        "username": "Jose",
        "full_name": "Jose Eduardo Arrucha Álvarez",
        "email": "jose.arruchaal@alumno.buap.mx",
        "phone": "2213317079",
        "photo": "/sources/Yosselin.JPEG",
        "disabled": False,
        "password": "$2a$12$oD4C5e9ymHoBk7gNabQ0EO9KbRkwDoBbkp8KWRmq4tsijtYmmwws2",
    },
}


# 1 Función para regresar el usuario completo de la base de datos (users_db), con contraseña encriptada
def search_user_db(username: str):
    if username in users_db:
        # ** devuelve todos los parámetros del usuario que coincida con username
        return UserDB(**users_db[username])

# 4 Función final para devolver usuario a la solicitud del backend


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# Funcion para devolver recurso estatico dependiendo del usuario


    # 3 Esta es la dependencia para buscar al usuario


async def auth_user(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Credenciales de autenticación inválidas")

    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticación inválidas")
    return search_user(username)

# 2 Función para determinar si usuario esta inactivo


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user


@app.post("/login/")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # Busca en la base de datos "users_db" el username que se ingreso en la forma
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    # Se obtienen los atributos incluyendo password del usuario que coincida el username de la forma
    user = search_user_db(form.username)

    # user.password es la contraseña encriptada en la base de datos
    # form.password es la contraseña original que viene en formulario
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="La contraseña no es correcta")
    # Creamos expiración de 1 min a partir de la hora actual
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    # Tiempo de expiración: hora actual mas 1 minuto
    expire = datetime.utcnow()+access_token_expiration

    access_token = {"sub": user.username, "exp": expire}
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@app.get("/users/me/")
async def me(user: User = Depends(current_user)):
    username = user.username
    if username in users_db:
        url = "sources/"+username+".JPEG"
        return FileResponse(url)
    return user



# http://127.0.0.1:8000/login/

# username:Freddy
# password:1234

# http://127.0.0.1:8000/me/

# -uvicorn 7_jwt_auth_users:app --reload

@app.get("/", response_class=HTMLResponse)
async def get_login_page():
    return FileResponse("login.html")

@app.get("/styles.css", response_class=HTMLResponse)
async def get_styles():
    return FileResponse("styles.css")

@app.get("/user/info", response_model=User)
async def get_user_info(user: User = Depends(current_user)):
    return user


token = "your_bearer_token_here"

headers = {
    "Authorization": f"Bearer {token}"
}

##response = requests.get("http://127.0.0.1:8000/user/info", headers=headers)

##if response.status_code == 200:
##    user_info = response.json()
##    print("User Info:")
##    print(user_info["photo"])
##    print("Username:", user_info["username"])
##    print("Phone:", user_info["phone"])
##    print("Email:", user_info["email"])
##else:
##    print("Failed to retrieve user information. Status code:", response.status_code)
