from app.auth.service import oauth2_scheme, AuthService
from app.pizzeria.service import PizzeriaService
from app.pizzeria.models import Pizza, PizzaUpdateRequest

from fastapi import Depends


def get_all_pizzas(service: PizzeriaService = Depends()):
    return service.get_all_pizzas()


def get_pizza(pizza_name: str, service: PizzeriaService = Depends()):
    return service.get_pizza(pizza_name)


def add_pizza(
    pizza: Pizza,
    token: str = Depends(oauth2_scheme),
    service: PizzeriaService = Depends(),
    auth_service: AuthService = Depends(),
):
    auth_service.verify_user(token)
    return service.add_pizza(pizza)


def delete_pizza(
    pizza_name: str,
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(),
    service: PizzeriaService = Depends()
):
    auth_service.verify_user(token)
    return service.delete_pizza(pizza_name)


def update_pizza(
    pizza_name: str,
    update_data: PizzaUpdateRequest,
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(),
    service: PizzeriaService = Depends()
):
    auth_service.verify_user(token)
    return service.update_pizza(pizza_name, update_data)
