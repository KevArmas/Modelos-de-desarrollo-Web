from fastapi import FastAPI
from routers import CRUD1, CRUD2, CRUD3, CRUD4, CRUD5, CRUD6, CRUD7, CRUD8, CRUD9, CRUD10

app = FastAPI()

app.include_router(CRUD1.router)
app.include_router(CRUD2.router)
app.include_router(CRUD3.router)
app.include_router(CRUD4.router)
app.include_router(CRUD5.router)
app.include_router(CRUD6.router)
app.include_router(CRUD7.router)
app.include_router(CRUD8.router)
app.include_router(CRUD9.router)
app.include_router(CRUD10.router)

@app.get("/")

async def imprimir():