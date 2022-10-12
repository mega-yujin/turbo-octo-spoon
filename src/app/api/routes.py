from fastapi import APIRouter, FastAPI
from app.auth.models import AuthResponse


def setup_routes(app: FastAPI) -> None:
    auth_router = APIRouter(prefix='/auth')
    auth_router.api_route(path='', methods=['POST'], response_model=AuthResponse)

    pizza_router = APIRouter(prefix='/pizza')
    pizza_router.api_route(path='', methods=['GET'], response_model=...)

    orders_router = APIRouter(prefix='/orders')
    orders_router.api_route(path='', methods=['GET', 'POST'], response_model=...)

    user_router = APIRouter(prefix='/user')
    user_router.api_route(path='', methods=['GET'], response_model=...)
    user_router.api_route(path='/register', methods=['POST'], response_model=...)

    app.include_router(auth_router)
