from fastapi import APIRouter, FastAPI


def setup_routes(app: FastAPI) -> None:
    auth_router = APIRouter(prefix='/auth')
    auth_router.api_route(path='', methods=['POST'], response_model=...)

    orders_router = APIRouter(prefix='/orders')
    orders_router.api_route(path='/get')
    orders_router.api_route(path='/make')

    app.include_router(auth_router)
