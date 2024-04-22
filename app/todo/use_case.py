from typing import List
from fastapi import HTTPException
from passlib.context import CryptContext
from .scheme import (
    RequestTodo,
    ResponseTodo,
    insert,
    get_all,
    get_by_id,
    get_by_user_id,
    update,
    delete,
)


def get_todo_all() -> List[ResponseTodo]:
    exit_todos = get_all()
    return exit_todos


def get_todo_by_id(todo_id: str) -> ResponseTodo:
    exit_todo = get_by_id(todo_id)
    return exit_todo


def get_todo_by_user_id(user_id: str) -> List[ResponseTodo]:
    exit_todos = get_by_user_id(user_id)
    return exit_todos


def create_todo(todo: RequestTodo) -> ResponseTodo:
    new_todo = insert(todo)
    return new_todo


def update_todo(todo_id: str, todo: RequestTodo) -> ResponseTodo:
    updated_todo = update(todo_id, todo)
    return updated_todo


def delete_todo(todo_id: str):
    delete(todo_id)
    return {"message": "Todo deleted successfully"}
