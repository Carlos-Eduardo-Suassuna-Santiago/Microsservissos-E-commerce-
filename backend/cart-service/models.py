from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # ID do usuário dono do carrinho
    product_id = Column(Integer)
    quantity = Column(Integer)
