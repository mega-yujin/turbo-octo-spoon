from app.api.models import ORMBaseModel, BaseResponse
from typing import Optional
from pydantic import Field, UUID4
from uuid import uuid4


class PizzaCategory(ORMBaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    name: str


class Ingredient(ORMBaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    name: str


class Pizza(ORMBaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    name: str
    category: Optional[PizzaCategory]
    description: Optional[str]
    price: float
    calories: int
    weight: int
    ingredients: list[Ingredient]


class PizzaUpdateRequest(ORMBaseModel):
    id: Optional[str]
    name: Optional[str]
    category: Optional[str]
    description: Optional[str]
    price: Optional[float]
    calories: Optional[int]
    weight: Optional[int]
    ingredients: Optional[list[Ingredient]]


class PizzaAddedResponse(BaseResponse):
    detail: str = Field(default='pizza added')
    pizza: Optional[Pizza]


class PizzaFoundResponse(BaseResponse):
    detail: str = Field(default='pizza found')
    pizza: Optional[Pizza]


class PizzaDeletedResponse(BaseResponse):
    detail: str = Field(default='pizza deleted successfully')


class PizzaUpdatedResponse(BaseResponse):
    detail: str = Field(default='pizza updated successfully')
    pizza: Optional[Pizza]
