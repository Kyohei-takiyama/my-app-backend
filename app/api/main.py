from fastapi import APIRouter
from user.views import router as user_router

router = APIRouter()

# 認証API
# TodoAPI
# ユーザーAPI
router.include_router(user_router)
