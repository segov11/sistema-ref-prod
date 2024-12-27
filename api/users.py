from fastapi import APIRouter, HTTPException
from models import User

router = APIRouter()

# Simulación de Base de Datos en Memoria
users_db = {}

@router.post("/", response_model=User)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    users_db[user.id] = user
    return user

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    users_db[user_id] = updated_user
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    del users_db[user_id]
    return {"message": "Usuario eliminado exitosamente"}