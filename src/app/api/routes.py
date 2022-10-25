from fastapi import APIRouter, FastAPI

from app.auth.handlers import get_user_data, login, register
from app.auth.models import AuthResponse, User
from app.pizzeria.handlers import get_all_pizzas, get_pizza, add_pizza, delete_pizza
from app.pizzeria.models import Pizza, PizzaAddedResponse, PizzaFoundResponse, PizzaDeletedResponse
from app.orders.handlers import update_order, add_order, get_active_orders, get_all_orders
from app.orders.models import Order, ActiveOrdersResponse, OrderAddResponse, OrderUpdateResponse
from app.system.handlers import check_status


def setup_routes(app: FastAPI) -> None:
    system_monitoring_router = APIRouter(prefix='/health', tags=['System Monitoring'])
    system_monitoring_router.api_route(path='/check', methods=['GET'])(check_status)

    auth_router = APIRouter(prefix='/auth', tags=['Authorization'])
    auth_router.api_route(path='/login', methods=['POST'], response_model=AuthResponse)(login)
    auth_router.api_route(path='/register', methods=['POST'], response_model=AuthResponse)(register)
    auth_router.api_route(path='/user', methods=['GET'], response_model=User)(get_user_data)

    pizza_router = APIRouter(prefix='/pizza', tags=['Pizzeria management'])
    pizza_router.api_route(path='', methods=['GET'], response_model=list[Pizza])(get_all_pizzas)
    pizza_router.api_route(path='', methods=['POST'], response_model=PizzaAddedResponse)(add_pizza)
    pizza_router.api_route(path='/{pizza_name}', methods=['GET'], response_model=PizzaFoundResponse)(get_pizza)
    pizza_router.api_route(path='/{pizza_name}', methods=['DELETE'], response_model=PizzaDeletedResponse)(delete_pizza)

    orders_router = APIRouter(prefix='/orders', tags=['Orders management'])
    orders_router.api_route(path='/history', methods=['GET'], response_model=list[Order])(get_all_orders)
    orders_router.api_route(path='/active', methods=['get'], response_model=ActiveOrdersResponse)(get_active_orders)
    orders_router.api_route(path='/add', methods=['POST'], response_model=OrderAddResponse)(add_order)
    orders_router.api_route(path='/{order_id}', methods=['PATCH'], response_model=OrderUpdateResponse)(update_order)

    app.include_router(auth_router)
    app.include_router(pizza_router)
    app.include_router(orders_router)
    app.include_router(system_monitoring_router)
