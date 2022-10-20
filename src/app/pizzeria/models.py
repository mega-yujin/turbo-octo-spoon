from app.api.models import ORMBaseModel
from typing import Optional


class PizzaCategory(ORMBaseModel):
    id: str
    name: str


class Ingredient(ORMBaseModel):
    id: str
    name: str


class Pizza(ORMBaseModel):
    id: str
    name: str
    category: Optional[str]
    description: str
    price: float
    calories: int
    weight: int
    ingredients: list[Ingredient]
