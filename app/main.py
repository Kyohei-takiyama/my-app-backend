import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.main import router as api_router
from app.core.config import get_env

app = FastAPI(prefix="/", tags=["healthcheck"])


# TODO:Middlewareを用意する
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
@app.get("/health")
async def health_check():
    return {"message": "api is running"}


app.include_router(api_router)

# ログ設定
root_logger = logging.getLogger("app")
handler = logging.StreamHandler()
# root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)
print(f"load env:::::::::{get_env()}")

# TODO:例外ハンドラーを用意する
# exceptions.init_app(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# from fastapi import FastAPI, HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from passlib.context import CryptContext
# from jose import jwt

# app = FastAPI()
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # 仮のユーザーデータベース
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "hashed_password": pwd_context.hash("secret"),
#     }
# }

# def authenticate_user(username: str, password: str):
#     user = fake_users_db.get(username)
#     if not user:
#         return False
#     if not pwd_context.verify(password, user['hashed_password']):
#         return False
#     return user

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     token = jwt.encode({"sub": user["username"]}, "secret_key", algorithm="HS256")
#     return {"access_token": token, "token_type": "bearer"}
