from datetime import datetime, timedelta

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table, DateTime
from sqlalchemy.orm import relationship

from src.app.system.database import Base


class UsersTable(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    orders = relationship('OrdersTable')


pizza_ingredient_table = Table(
    "pizza_ingredient",
    Base.metadata,
    Column("pizza_id", ForeignKey("pizzas.id"), primary_key=True),
    Column("ingredient_id", ForeignKey("ingredients.id"), primary_key=True),
)

orders_pizzas_table = Table(
    "orders_pizzas",
    Base.metadata,
    Column('order_id', ForeignKey('orders.id'), primary_key=True),
    Column('pizza_id', ForeignKey('pizzas.id'), primary_key=True),
)


class PizzasTable(Base):
    __tablename__ = "pizzas"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category_id = Column(String, ForeignKey('categories.id'))
    description = Column(String)
    price = Column(Float)
    calories = Column(Integer)
    weight = Column(Integer)

    ingredients = relationship("IngredientsTable", secondary=pizza_ingredient_table, back_populates="pizzas")
    category = relationship('CategoriesTable')


class CategoriesTable(Base):
    __tablename__ = 'categories'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)


class IngredientsTable(Base):
    __tablename__ = "ingredients"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)

    pizzas = relationship("PizzasTable", secondary=pizza_ingredient_table, back_populates="ingredients")


class OrdersTable(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'))
    city = Column(String)
    street = Column(String)
    building = Column(String)
    delivery_time = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(minutes=30))
    total_price = Column(Float)
    is_delivered = Column(Boolean, default=False)

    ordered_items = relationship('PizzasTable', secondary=orders_pizzas_table)
