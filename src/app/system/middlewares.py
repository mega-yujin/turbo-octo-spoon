from typing import Callable, Awaitable

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.auth.service import oauth2_scheme, AuthService

AUTH_REQUIRED = []


def handle_http_exceptions(exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        {'detail': exc.detail},
        status_code=exc.status_code,
        headers=getattr(exc, 'headers', None)
    )


class AuthCheckMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, endpoints: list[str], dispatch=None):
        super().__init__(app, dispatch)
        self.endpoints_to_check = endpoints
        self.auth_service = AuthService()

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        endpoint = request.scope.get('path')
        if endpoint in self.endpoints_to_check:
            try:
                token = await oauth2_scheme(request)
                self.auth_service.get_current_active_user(token)
            except HTTPException as exc:
                handle_http_exceptions(exc)
        return await call_next(request)


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(AuthCheckMiddleware, endpoints=AUTH_REQUIRED)
