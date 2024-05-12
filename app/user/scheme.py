from typing import Optional, List
from fastapi import HTTPException
from sqlalchemy.orm import Session, sessionmaker
from app.migration.models import User, Engine
from uuid import uuid4
from pydantic import BaseModel, UUID4
from datetime import datetime

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


class RequestUser(BaseModel):
    username: str
    password: str


class UpdateUser(BaseModel):
    username: Optional[str]
    password: Optional[str]


class ResponseUser(BaseModel):
    user_id: UUID4
    username: str
    password: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


def get_all() -> List[ResponseUser]:
    db = SessionLocal()
    db_users = db.query(User).all()
    if db_users is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.close()
    return db_users


def get_by_id(user_id: str) -> ResponseUser:
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.close()
    return db_user


def insert(user: RequestUser) -> ResponseUser:
    db = SessionLocal()

    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user


def update(user_id: str, user: UpdateUser) -> ResponseUser:
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user.username != "":
        db_user.username = user.username
    if user.password != "":
        db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user


def delete(user_id: str):
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    db.close()
