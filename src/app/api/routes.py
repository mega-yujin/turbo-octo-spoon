from fastapi import APIRouter, FastAPI
from app.auth.models import AuthResponse, User
from app.auth.handlers import get_user_data, login, register
from app.pizzeria.handlers import get_all_pizzas, get_pizza, add_pizza, delete_pizza
from app.orders.handlers import delete_order, create_order, get_order, get_all_orders


def setup_routes(app: FastAPI) -> None:
    auth_router = APIRouter(prefix='/auth')
    auth_router.api_route(path='/login', methods=['POST'], response_model=AuthResponse)(login)
    auth_router.api_route(path='/register', methods=['POST'], response_model=AuthResponse)(register)
    auth_router.api_route(path='/user', methods=['GET'], response_model=User)(get_user_data)

    # pizza_router = APIRouter(prefix='/pizza')
    # pizza_router.api_route(path='', methods=['GET'], response_model=...)(get_all_pizzas)
    # pizza_router.api_route(path='', methods=['POST'], response_model=...)(add_pizza)
    # pizza_router.api_route(path='{pizza_id}', methods=['GET'], response_model=...)(get_pizza)
    # pizza_router.api_route(path='{pizza_id}', methods=['DELETE'], response_model=...)(delete_pizza)
    #
    # orders_router = APIRouter(prefix='/orders')
    # orders_router.api_route(path='', methods=['GET'], response_model=...)(get_all_orders)
    # orders_router.api_route(path='', methods=['POST'], response_model=...)(create_order)
    # orders_router.api_route(path='{order_id}', methods=['get'], response_model=...)(get_order)
    # orders_router.api_route(path='{order_id}', methods=['DELETE'], response_model=...)(delete_order)

    app.include_router(auth_router)
