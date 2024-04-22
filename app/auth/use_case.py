from fastapi import Depends
from datetime import timedelta, datetime
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker
from migration.models import User, Engine
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from core.config import get_env
from jose import jwt


class Token(BaseModel):
    access_token: str
    token_type: str


env_values = get_env()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def authenticate_user(username: str, password: str) -> User:
    print(f"authenticate_user ::: {username}, {password}")
    db: Session = next(get_db())
    user = db.query(User).filter(User.name == username).first()
    if not user:
        return None
    if not bycrypt_context.verify(password, user.password):
        return None
    return user


def create_access_token(username: str, user_id: str, expires_delta: timedelta):
    print(f"create_access_token ::: {username}, {user_id}, {expires_delta}")
    to_encode = {
        "sub": username,
        "user_id": str(user_id),
        "exp": datetime.now() + expires_delta,
    }
    return jwt.encode(to_encode, env_values.SECRET_KEY, algorithm=env_values.ALGORITHM)
