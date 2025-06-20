from pydantic import BaseModel
from typing import List

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItemCreate]

class OrderItemOut(OrderItemCreate):
    id: int
    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    items: List[OrderItemOut]

    class Config:
        orm_mode = True

class OrderStatusUpdate(BaseModel):
    status: str
