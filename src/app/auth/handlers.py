from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.authentication import create_access_token, authenticate_user, get_current_active_user
from app.auth.models import User
from app.config import fake_users_db, ACCESS_TOKEN_EXPIRE_MINUTES
from app.auth.models import Token, AuthResponse


async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return AuthResponse(
        result="ok",
        detail="authentication success",
        token=Token(
            access_token=access_token,
            token_type="bearer",
        ),
    )


# @app.get("/users/me/", response_model=User)
async def get_user_data(current_user: User = Depends(get_current_active_user)):
    return current_user


async def register(request):
    pass
