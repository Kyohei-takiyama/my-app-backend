from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from .model import RequestUser, ResponseUser, insert, get_all, get_by_id, update, delete


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


def update_user(user_id: str, user: RequestUser) -> ResponseUser:
    if user.name is None and user.password is None:
        raise HTTPException(status_code=400, detail="name or password is required")
    if user.password != "":
        user.password = hash_password(user.password)
    updated_user = update(user_id, user)
    return updated_user


def delete_user(user_id: str):
    delete(user_id)
    return {"message": "User deleted successfully"}


def hash_password(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)
