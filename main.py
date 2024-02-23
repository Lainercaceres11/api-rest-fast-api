from fastapi import FastAPI

#Router
from routes import products, users, auth_basic, jwt_auth, user_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Router
app.include_router(products.router)
app.include_router(users.router)
app.include_router(auth_basic.router)
app.include_router(jwt_auth.router)
app.include_router(user_db.router)


#Importar archivos estaticos 
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola FastAPi"

#Devolvemos un JSON a /url
@app.get("/url")
async def url():
    return {"url": "https://github.com/Lainercaceres11"}

#Deploy a deta 
#Instalar deta en windows
#1: #iwr https://deta.space/assets/space-cli.ps1 -useb | iex
#2: deta login
#: deta new
#3: deta deploy
