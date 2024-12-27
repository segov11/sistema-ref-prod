from fastapi import APIRouter, HTTPException
from models import Product

router = APIRouter()

# Simulación de Base de Datos en Memoria
products_db = {}

@router.post("/", response_model=Product)
def create_product(product: Product):
    if product.id in products_db:
        raise HTTPException(status_code=400, detail="Producto ya existe")
    products_db[product.id] = product
    return product

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    products_db[product_id] = updated_product
    return updated_product

@router.delete("/{product_id}")
def delete_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    del products_db[product_id]
    return {"message": "Producto eliminado exitosamente"}