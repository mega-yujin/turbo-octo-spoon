from typing import Union, Optional
from uuid import uuid4

from pydantic import Field, UUID4

from app.api.models import ORMBaseModel


class BaseUser(ORMBaseModel):
    username: str
    email: Optional[str] = None


class User(BaseUser):
    id: UUID4 = Field(default_factory=uuid4)
    is_active: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


class UserCreate(BaseUser):
    password: str


class Token(ORMBaseModel):
    access_token: str
    token_type: str


class TokenData(ORMBaseModel):
    username: Union[str, None] = None


class AuthResponse(ORMBaseModel):
    result: str
    detail: str
    token: Token
