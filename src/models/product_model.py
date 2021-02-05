from sqlalchemy import Column, String, Float
from sqlalchemy.orm import validates
from src.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = 'PRODUCT'

    name = Column('name', String(length=100), nullable=False)
    price = Column('price', Float, nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Invalid type for name')
        elif not name.strip():
            raise ValueError("Name can't be empty")
        elif len(name) > 100:
            raise ValueError("Name can't be larger than 100 characters")
        return name

    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, float):
            raise TypeError('Invalid type for price')
        elif price <= 0:
            raise ValueError("Price can't be lower than 0")
        return price

    @validates('description')
    def validate_description(self, key, description):
        if description is not None:
            if len(description) > 255:
                raise ValueError("Description can't be larger than 255 characters")
        return description
