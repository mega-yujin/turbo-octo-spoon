from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import Field

from app.api.models import ORMBaseModel
from app.auth.models import User
from app.pizzeria.models import Pizza


class Order(ORMBaseModel):
    id: str = Field(default=str(uuid4))
    user_id: str
    city: str
    street: str
    building: str
    delivery_time: datetime
    total_price: float
    is_delivered: bool
    ordered_items: list[Pizza]


class UserWithOrders(User):
    orders: Optional[list[Order]]
