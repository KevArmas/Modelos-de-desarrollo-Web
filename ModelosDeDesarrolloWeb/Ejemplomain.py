from fastapi import FastAPI
app = FastAPI()
@app.get("/Git")
async def imprimir():
    return  {"Git_curso":"https://github.com/freddy-7777/Modelos_de_Desarrollo_WEB.git"}

