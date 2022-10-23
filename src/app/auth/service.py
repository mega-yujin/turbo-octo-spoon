from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.auth.models import UserInDB, User, Token, UserCreate
from app.config import AppSettings, get_settings
from app.system.database import get_db_session
from app.system.schemas import UsersTable

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

register_exception = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="Username already exists",
    headers={"WWW-Authenticate": "Bearer"},
)

inactive_user_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="User inactive",
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


class AuthService:
    def __init__(
            self,
            db_session: Session = Depends(get_db_session),
            settings: AppSettings = get_settings(),
    ):
        self.db_session = db_session
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.settings = settings

    def authenticate_user(self, username: str, password: str) -> Token:
        user: UserInDB = self._get_user(username)
        if user:
            self._verify_password(password, user.hashed_password)
        else:
            raise credentials_exception
        return self._create_access_token(user)

    def get_current_active_user(self, token: str) -> User:
        current_user = self.get_current_user(token)
        if not current_user.is_active:
            raise inactive_user_exception
        return current_user

    def get_current_user(self, token: str) -> User:
        try:
            payload = jwt.decode(token, self.settings.SECRET_KEY, algorithms=[self.settings.ALGORITHM])
            username: str = payload.get('user_data').get('username')
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = self._get_user(username)
        if user is None:
            raise credentials_exception
        return user

    def register_user(self, new_user: UserCreate):
        user = self._get_user(new_user.username)
        if user:
            raise register_exception
        user_in_db = UsersTable(
            id=str(uuid4()),
            username=new_user.username,
            email=new_user.email,
            hashed_password=self._get_password_hash(new_user.password),
            is_active=True,
        )
        self.db_session.add(user_in_db)
        self.db_session.commit()
        return self._create_access_token(UserInDB.from_orm(user_in_db))

    def _create_access_token(self, user: UserInDB) -> Token:
        if self.settings.ACCESS_TOKEN_EXPIRE_MINUTES:
            expire = datetime.utcnow() + timedelta(minutes=self.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        data = {
            'user_data': user.dict(),
            'exp': expire
        }
        encoded_jwt = jwt.encode(data, self.settings.SECRET_KEY, algorithm=self.settings.ALGORITHM)
        return Token(access_token=encoded_jwt, token_type='bearer')

    def _verify_password(self, plain_password: str, hashed_password: str) -> None:
        if not self.pwd_context.verify(plain_password, hashed_password):
            raise credentials_exception

    def _get_password_hash(self, password) -> str:
        return self.pwd_context.hash(password)

    def _get_user(self, username: str) -> Optional[UserInDB]:
        user = None
        user_from_db = self.db_session.query(UsersTable).filter(UsersTable.username == username).first()
        if user_from_db:
            user = UserInDB.from_orm(user_from_db)
        return user
