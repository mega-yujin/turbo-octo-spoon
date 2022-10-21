from datetime import datetime

from pydantic import BaseModel
from typing import Optional, Union


class ORMBaseModel(BaseModel):
    class Config:
        orm_mode = True


class User(ORMBaseModel):
    # id: UUID
    id: str
    username: str
    email: Union[str, None] = None
    is_active: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


class Token(ORMBaseModel):
    access_token: str
    token_type: str


class TokenData(ORMBaseModel):
    username: Union[str, None] = None


class AuthResponse(ORMBaseModel):
    result: str
    detail: str
    token: Token


class PizzaCategory(ORMBaseModel):
    id: str
    name: str


class Ingredient(ORMBaseModel):
    id: str
    name: str


class Pizza(ORMBaseModel):
    id: str
    name: str
    category: Optional[PizzaCategory]
    description: str
    price: float
    calories: int
    weight: int
    ingredients: list[Ingredient]


class Order(ORMBaseModel):
    id: str
    user: User
    city: str
    street: str
    building: str
    delivery_time: datetime
    total_price: float
    is_delivered: bool
    ordered_items: list[Pizza]


class UserWithOrders(User):
    orders: Optional[list[Order]]
