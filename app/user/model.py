from typing import Optional, List
from fastapi import HTTPException
from sqlalchemy.orm import Session, sessionmaker
from migration.models import User, Engine
from uuid import uuid4
from pydantic import BaseModel

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


class RequestUser(BaseModel):
    name: str
    password: str


class ResponseUser(BaseModel):
    user_id: str
    name: str
    password: str
    created_at: Optional[str]
    updated_at: Optional[str]


# # 依存関係
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


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

    new_user = User(name=user.name, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user
