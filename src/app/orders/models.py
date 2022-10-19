from pydantic import BaseModel
from app.api.models import ORMBaseModel
from app.auth.models import User
from app.pizzeria.models import Pizza


class Order(ORMBaseModel):
    id: str
    user: User
    data: list[Pizza]
    price: float
    calories: int
