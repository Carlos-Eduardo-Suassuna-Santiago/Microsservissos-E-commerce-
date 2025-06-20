from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import Order, OrderItem
from schemas import OrderCreate, OrderOut, OrderStatusUpdate

router = APIRouter()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orders", response_model=OrderOut)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    total_price = sum(item.price * item.quantity for item in order_data.items)
    new_order = Order(user_id=order_data.user_id, total_price=total_price)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order_data.items:
        db_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(db_item)
    db.commit()

    items = db.query(OrderItem).filter(OrderItem.order_id == new_order.id).all()
    return OrderOut(id=new_order.id, user_id=new_order.user_id, total_price=new_order.total_price, status=new_order.status, items=items)

@router.get("/orders/{user_id}", response_model=list[OrderOut])
def get_orders(user_id: int, db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    result = []
    for order in orders:
        items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
        result.append(OrderOut(
            id=order.id,
            user_id=order.user_id,
            total_price=order.total_price,
            status=order.status,
            items=items
        ))
    return result

@router.get("/order/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
    return OrderOut(id=order.id, user_id=order.user_id, total_price=order.total_price, status=order.status, items=items)

@router.put("/order/{order_id}/status", response_model=OrderOut)
def update_order_status(order_id: int, status_update: OrderStatusUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = status_update.status
    db.commit()
    db.refresh(order)
    items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
    return OrderOut(id=order.id, user_id=order.user_id, total_price=order.total_price, status=order.status, items=items)
