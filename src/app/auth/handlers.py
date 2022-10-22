from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.models import UserCreate
from app.auth.models import Token, AuthResponse
from app.auth.service import AuthService


def login(login_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()):
    access_token = service.authenticate_user(login_data.username, login_data.password)
    return AuthResponse(
        result="ok",
        detail="authentication success",
        token=access_token,
    )


async def get_user_data(request: Request, service: AuthService = Depends()):
    return await service.get_current_active_user(request)


def register(user_data: UserCreate, service: AuthService = Depends()):
    return AuthResponse(
            result="ok",
            detail="authentication success",
            token=Token(
                access_token=service.register_user(user_data),
                token_type="bearer",
            ),
        )

# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return AuthResponse(
#         result="ok",
#         detail="authentication success",
#         token=Token(
#             access_token=access_token,
#             token_type="bearer",
#         ),
#     )


# async def get_user_data(current_user: User = Depends(get_current_active_user)):
#     return current_user
