from pydantic import BaseModel, EmailStr
from typing import List

class Product(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price: float
    stock: int

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    preferences: List[str]