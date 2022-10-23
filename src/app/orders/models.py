from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import Field, UUID4

from app.api.models import ORMBaseModel
from app.auth.models import User
from app.pizzeria.models import Pizza


class Order(ORMBaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    user_id: UUID4
    city: str
    street: str
    building: str
    delivery_time: datetime
    total_price: float
    is_delivered: bool
    ordered_items: list[Pizza]


class UserWithOrders(User):
    orders: Optional[list[Order]]
