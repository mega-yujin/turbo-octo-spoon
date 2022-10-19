from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
# from uuid import uuid4

from src.app.system.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


pizza_ingredient_table = Table(
    "pizza_ingredient",
    Base.metadata,
    Column("pizza_id", ForeignKey("pizzas.id"), primary_key=True),
    Column("ingredient_id", ForeignKey("ingredients.id"), primary_key=True),
)


class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(String)
    description = Column(String)
    price = Column(Float)
    calories = Column(Integer)
    weight = Column(Integer)

    ingredients = relationship("Ingredient", secondary=pizza_ingredient_table, back_populates="pizza")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)

    pizza = relationship("Pizza", secondary=pizza_ingredient_table, back_populates="ingredients")


class Order(Base):
    __tablename__ = "orders"


class OrderPizza(Base):
    __tablename__ = "order_pizzas"
