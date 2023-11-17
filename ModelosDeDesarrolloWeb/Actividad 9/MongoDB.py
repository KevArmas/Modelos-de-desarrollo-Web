from fastapi import FastAPI
from routers import router_db

app = FastAPI()
app.include_router(router_db.router)