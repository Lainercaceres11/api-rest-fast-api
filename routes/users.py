from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

#Modelo de usuarios
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
def search_user(id: int):
    try:
       users = filter(lambda user: user.id == id, user_list)
       return list(users)[0]
    except:
       return {"error": "No se ha encontrado el usuario"}

user_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Joselu", surname="Dev", url="https://mouredev.com", age=35),
              User(id=3, name="Lainer", surname="Dahlberg", url="https://haakon.com", age=33)]

#Endpoints
@router.get("/")
async def root():
    return "Hola users"

@router.get("/users")
async def users():
    return user_list


#Busca el usuario con el id del path
@router.get("/user/{id}")
async def user_by_id(id: int):
    return search_user(id)
 
 #Busca el usuario por el nombre de query params
@router.get("/user/")
async def user_by_name(name: str):
   try:
       users = filter(lambda user: user.name == name, user_list)
       return list(users)[0]
   except:
       return {"error": "No se ha encontrado el usuario"}
   
#Agregar usuario
@router.post("/user", response_model=User, status_code=201)
async def add_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="No se pudo crear el usuario")
    else:
        user_list.append(user)
    return user
 
 #Actualiza el usuario   
@router.put("/user")
async def update_user(user: User):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
            
    if not found:
        return {"msg": "No se ha actualizado el usuario"}
    
    return user

 #elimina el usuario   
@router.delete("/user/{id}")
async def delete_user(id: int):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
            
    if not found:
        return {"msg": "No se ha eliminado el usuario"}
    
    return id
   
   

 
    