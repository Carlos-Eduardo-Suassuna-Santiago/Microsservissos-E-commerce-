from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import CartItem
from schemas import CartItemCreate, CartItemUpdate, CartItemOut

router = APIRouter()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cart", response_model=CartItemOut)
def add_to_cart(item: CartItemCreate, db: Session = Depends(get_db)):
    db_item = CartItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/cart/{user_id}", response_model=list[CartItemOut])
def get_cart(user_id: int, db: Session = Depends(get_db)):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

@router.put("/cart/{item_id}", response_model=CartItemOut)
def update_quantity(item_id: int, item: CartItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(CartItem).get(item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.quantity = item.quantity
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/cart/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(CartItem).get(item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item removed from cart"}

@router.delete("/cart/user/{user_id}")
def clear_cart(user_id: int, db: Session = Depends(get_db)):
    items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    for item in items:
        db.delete(item)
    db.commit()
    return {"message": "Cart cleared"}
