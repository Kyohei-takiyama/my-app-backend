from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session, sessionmaker
from migration.models import User, Engine
from .model import RequestUser, ResponseUser, insert, get_all, get_by_id


def get_user_all() -> List[ResponseUser]:
    exit_users = get_all()
    return exit_users


def get_user_by_id(user_id: str) -> ResponseUser:
    exit_user = get_by_id(user_id)
    return exit_user


def create_user(user: RequestUser) -> ResponseUser:
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    inserted_user = insert(user)
    return inserted_user


def hash_password(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)
