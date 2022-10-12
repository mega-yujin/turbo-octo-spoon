from pydantic import BaseModel, validate_email
from uuid import uuid4
from typing import Optional


@validate_email
class User(BaseModel):
    id: uuid4
    username: str
    password: str
    email: str


class AuthRequest(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    result: str
    detail: Optional[str]
