from app.api.models import ORMBaseModel
from typing import Optional
from pydantic import Field
from uuid import uuid4


class PizzaCategory(ORMBaseModel):
    id: str
    name: str


class Ingredient(ORMBaseModel):
    id: str = Field(default=str(uuid4()))
    name: str


class Pizza(ORMBaseModel):
    id: str = Field(default=str(uuid4()))
    name: str
    category: Optional[PizzaCategory]
    description: str
    price: float
    calories: int
    weight: int
    ingredients: list[Ingredient]
