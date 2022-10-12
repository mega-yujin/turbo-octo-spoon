from pydantic import BaseModel
from uuid import uuid4
from app.auth.models import User


class PizzaCategory:
    id: uuid4
    name: str


class Pizza(BaseModel):
    id: uuid4
    name: str
    category: PizzaCategory
    description: str
    price: float
    calories: int


class Order(BaseModel):
    id: uuid4
    user: User
    data: list[Pizza]
    price: float
    calories: int
