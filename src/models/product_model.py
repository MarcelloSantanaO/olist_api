from sqlalchemy import Column, String, Float
from src.models.base_model import BaseModel
class Product(BaseModel):
    __tablename__ = 'PRODUCT'

    name = Column('name', String(length=100), nullable=False)
    price = Column('price', Float, nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name: str, price: float, description: str = None):
        self.name = name
        self.price = price
        self.description = description
