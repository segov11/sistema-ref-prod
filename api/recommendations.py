from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models import Product
from api.users import users_db
from api.products import products_db

router = APIRouter()

@router.get("/{user_id}", response_model=List[Product])
def get_recommendations(user_id: int, max_price: Optional[float] = None):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    recommended = []

    # Basado en las preferencias
    for product in products_db.values():
        if product.category in user.preferences and product.stock > 0:
            if max_price is None or product.price <= max_price:
                recommended.append(product)

    # Si no hay historial o preferencias, recomendar más populares
    if not recommended:
        recommended = sorted(products_db.values(), key=lambda x: -x.stock)[:5]

    return recommended