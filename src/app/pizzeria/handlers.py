from app.auth.service import oauth2_scheme, AuthService
from app.pizzeria.service import PizzeriaService
from app.pizzeria.models import Pizza, PizzaAddedResponse

from fastapi import Depends


def get_all_pizzas(service: PizzeriaService = Depends()):
    return service.get_all_pizzas()


def get_pizza():
    pass


def add_pizza(
    pizza: Pizza,
    token: str = Depends(oauth2_scheme),
    service: PizzeriaService = Depends(),
    auth_service: AuthService = Depends(),
):
    auth_service.verify_user(token)
    return service.add_pizza(pizza)


def delete_pizza(pizza_name, token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends()):
    auth_service.verify_user(token)
    pass
