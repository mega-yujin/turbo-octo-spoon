from pydantic import BaseModel, validate_email
from uuid import uuid4
from typing import Optional, Union


@validate_email
class User(BaseModel):
    id: uuid4
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class AuthRequest(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    result: str
    detail: Optional[str]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserInDB(User):
    hashed_password: str
