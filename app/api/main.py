from fastapi import APIRouter
from user.views import router as user_router
from auth.views import router as auth_router

router = APIRouter()

# TodoAPI
# ユーザーAPI
router.include_router(user_router)
# 認証API
router.include_router(auth_router)
