from fastapi import APIRouter
from app.user.views import router as user_router
from app.auth.views import router as auth_router
from app.todo.views import router as todo_router

router = APIRouter()

# TodoAPI
router.include_router(todo_router)
# ユーザーAPI
router.include_router(user_router)
# 認証API
router.include_router(auth_router)
