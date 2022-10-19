from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Union


class User(BaseModel):
    # id: UUID
    id: str
    username: str
    email: Union[str, None] = None
    is_active: Union[bool, None] = None

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class AuthResponse(BaseModel):
    result: str
    detail: str
    token: Token
