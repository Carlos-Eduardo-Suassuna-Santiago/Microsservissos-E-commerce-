from pydantic import BaseModel

class CartItemCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartItemUpdate(BaseModel):
    quantity: int

class CartItemOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int

    class Config:
        form_mode = True
