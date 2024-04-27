from pydantic import BaseModel, UUID4
from typing import Optional, List
from fastapi import HTTPException
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime

from app.migration.models import Todo, Engine


class RequestTodo(BaseModel):
    title: str
    description: str
    status: str
    due_date: datetime
    priority: int
    tags: str
    is_archived: bool
    user_id: Optional[UUID4]


class ResponseTodo(BaseModel):
    title: str
    description: str
    status: str
    due_date: datetime
    priority: int
    tags: str
    is_archived: bool
    user_id: UUID4


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)


def get_all() -> List[ResponseTodo]:
    db = SessionLocal()
    db_todos = db.query(Todo).all()
    if db_todos is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.close()
    return db_todos


def get_by_id(todo_id: str) -> ResponseTodo:
    db = SessionLocal()
    db_todo = db.query(Todo).filter(Todo.todo_id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.close()
    return db_todo


def get_by_user_id(user_id: str) -> List[ResponseTodo]:
    db = SessionLocal()
    db_todos = db.query(Todo).filter(Todo.user_id == user_id).all()
    if db_todos is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.close()
    return db_todos


def insert(todo: RequestTodo):
    db = SessionLocal()
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        status=todo.status,
        # datetimeに変換する
        due_date=todo.due_date,
        priority=todo.priority,
        tags=todo.tags,
        is_archived=todo.is_archived,
        user_id=todo.user_id,
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    db.close()
    return new_todo


def update(todo_id: str, todo: RequestTodo):
    db = SessionLocal()
    db_todo = db.query(Todo).filter(Todo.todo_id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.title != "":
        db_todo.title = todo.title
    if todo.description != "":
        db_todo.description = todo.description
    if todo.status != "":
        db_todo.status = todo.status
    if todo.due_date != "":
        db_todo.due_date = todo.due_date
    if todo.priority != "":
        db_todo.priority = todo.priority
    if todo.tags != "":
        db_todo.tags = todo.tags
    if todo.is_archived != "":
        db_todo.is_archived = todo.is_archived
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo


def delete(todo_id: str):
    db = SessionLocal()
    db_todo = db.query(Todo).filter(Todo.todo_id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    db.close()
    return {"message": "Todo deleted successfully"}
