from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.migration.models import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.config import get_env
from .use_case import (
    Token,
    authenticate_user,
    create_access_token,
)

env_values = get_env()


router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_bearer = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


# jwtを使用して認証し、トークンを返す
@router.post("/token", response_model=Token)
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print(f"login_access_token ::: {form_data.username}, {form_data.password}")
    user: User = authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token = create_access_token(user.name, user.user_id, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}
