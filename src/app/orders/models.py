from datetime import datetime
from typing import Optional

from app.api.models import ORMBaseModel
from app.auth.models import User
from app.pizzeria.models import Pizza


class Order(ORMBaseModel):
    id: str
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
