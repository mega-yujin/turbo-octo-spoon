from app.pizzeria.service import PizzeriaService

from fastapi import Depends


def get_all_pizzas(service: PizzeriaService = Depends()):
    return service.get_all_pizzas()


def get_pizza():
    pass


def add_pizza():
    pass


def delete_pizza():
    pass
