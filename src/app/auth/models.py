from typing import Union

from app.api.models import ORMBaseModel


class User(ORMBaseModel):
    # id: UUID
    id: str
    username: str
    email: Union[str, None] = None
    is_active: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


class Token(ORMBaseModel):
    access_token: str
    token_type: str


class TokenData(ORMBaseModel):
    username: Union[str, None] = None


class AuthResponse(ORMBaseModel):
    result: str
    detail: str
    token: Token
