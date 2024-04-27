from fastapi import Depends, Request
from typing import List
from fastapi import HTTPException
from .use_case import (
    get_todo_all,
    get_todo_by_user_id,
    get_todo_by_id,
    create_todo,
    update_todo,
    delete_todo,
)
from .scheme import RequestTodo, ResponseTodo
from app.router import APIRouter
from app.user.use_case import get_user_by_id


router = APIRouter(prefix="/api/v1/todos", tags=["todos"])


@router.get("/")
async def retrieve_all() -> List[ResponseTodo]:
    return get_todo_all()


@router.get("/{id}")
async def retrieve_by_id(id) -> ResponseTodo:
    return get_todo_by_id(id)


@router.get("/{user_id}")
async def retrieve_by_user_id(user_id) -> ResponseTodo:
    return get_todo_by_user_id(user_id)


@router.post("/")
async def create(todo: RequestTodo) -> ResponseTodo:
    user = get_user_by_id(todo.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return create_todo(todo)


@router.put("/{todo_id}")
async def update(todo_id, todo: RequestTodo) -> ResponseTodo:
    return update_todo(todo_id, todo)


@router.delete("/{todo_id}")
async def delete(todo_id) -> dict:
    return delete_todo(todo_id)
