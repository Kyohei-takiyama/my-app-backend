from fastapi import Depends, Request
from typing import List
from .use_case import (
    get_user_all,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)
from .scheme import RequestUser, ResponseUser, UpdateUser
from router import APIRouter


router = APIRouter(prefix="/api/v1/users")


@router.get("/")
async def retrieve_all() -> List[ResponseUser]:
    return get_user_all()


@router.get("/{user_id}")
async def retrieve_by_id(user_id) -> ResponseUser:
    return get_user_by_id(user_id)


@router.post("/")
async def create(user: RequestUser) -> ResponseUser:
    return create_user(user)


@router.put("/{user_id}")
async def update(user_id, user: UpdateUser) -> ResponseUser:
    return update_user(user_id, user)


@router.delete("/{user_id}")
async def delete(user_id) -> dict:
    return delete_user(user_id)
