from uuid import UUID

from app.auth.service import AuthService, oauth2_scheme
from app.orders.service import OrdersService

from app.orders.models import OrderAddRequest, OrderUpdateRequest

from fastapi import Depends


def add_order(
    order: OrderAddRequest,
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(),
    orders_service: OrdersService = Depends(),
):
    user = auth_service.verify_user(token)
    return orders_service.add_order(order, user.id)


def update_order(
    order_id: UUID,
    order_update: OrderUpdateRequest,
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(),
    orders_service: OrdersService = Depends(),
):
    auth_service.verify_user(token)
    return orders_service.update_order(order_id, order_update)


def get_active_orders(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(),
    orders_service: OrdersService = Depends(),
):
    user = auth_service.verify_user(token)
    return orders_service.get_active_orders(user.id)


def get_all_orders(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(),
    orders_service: OrdersService = Depends(),
):
    user = auth_service.verify_user(token)
    return orders_service.get_all_orders(user.id)
