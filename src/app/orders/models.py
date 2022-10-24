from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from pydantic import Field, UUID4

from app.api.models import ORMBaseModel, BaseResponse
from app.auth.models import User
from app.pizzeria.models import Pizza


class OrderedPizza(ORMBaseModel):
    pizza_id: UUID4
    amount: int = Field(default=1)


class Order(ORMBaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    user_id: UUID4
    city: str
    street: str
    building: str
    delivery_time: datetime
    total_price: float
    is_delivered: bool = Field(default=False)
    ordered_items: list[OrderedPizza]


class UserWithOrders(User):
    orders: Optional[list[Order]]


class ActiveOrdersResponse(BaseResponse):
    detail: str = Field(default='Active orders found')
    orders: Optional[list[Order]]


class OrderAddResponse(BaseResponse):
    detail: str = Field(default='Order added')
    order: Optional[Order]


class OrderUpdateResponse(BaseResponse):
    detail: str = Field(default='Order updated successfully')
    order: Optional[Order]


class OrderAddRequest(ORMBaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    city: str
    street: str
    building: str
    delivery_time: datetime = Field(default=lambda: datetime.utcnow() + timedelta(minutes=30))
    ordered_items: list[OrderedPizza]


class OrderUpdateRequest(ORMBaseModel):
    id: UUID4
    city: Optional[str]
    street: Optional[str]
    building: Optional[str]
    delivery_time: Optional[datetime]
    is_delivered: Optional[bool]

