from fastapi import APIRouter
from user.views import router as user_router
from auth.views import router as auth_router
from todo.views import router as todo_router

router = APIRouter()

# TodoAPI
router.include_router(todo_router)
# ユーザーAPI
router.include_router(user_router)
# 認証API
router.include_router(auth_router)
