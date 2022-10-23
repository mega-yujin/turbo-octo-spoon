from app.pizzeria.service import PizzeriaService
from app.pizzeria.models import Pizza, PizzaCreatedResponse

from fastapi import Depends


def get_all_pizzas(service: PizzeriaService = Depends()):
    return service.get_all_pizzas()


def get_pizza():
    pass


def add_pizza(pizza: Pizza, service: PizzeriaService = Depends()):
    return service.add_pizza(pizza)


def delete_pizza():
    pass
