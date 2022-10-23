from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.models import UserCreate
from app.auth.models import Token, AuthResponse
from app.auth.service import AuthService, oauth2_scheme


def login(login_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()):
    access_token = service.authenticate_user(login_data.username, login_data.password)
    return AuthResponse(
        result="ok",
        detail="authentication success",
        token=access_token,
    )


def get_user_data(token: str = Depends(oauth2_scheme), service: AuthService = Depends()):
    return service.get_current_active_user(token)


def register(user_data: UserCreate, service: AuthService = Depends()):
    return AuthResponse(
            result="ok",
            detail="authentication success",
            token=Token(
                access_token=service.register_user(user_data),
                token_type="bearer",
            ),
        )
