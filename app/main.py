import uvicorn
from fastapi import FastAPI
from typing import List
from user.use_case import get_user_all, get_user_by_id, create_user
from user.model import RequestUser, ResponseUser

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/apiv1/users/")
async def retrieve_all() -> List[ResponseUser]:
    return get_user_all()


@app.get("/apiv1/users/{user_id}")
async def retrieve_by_id(user_id) -> ResponseUser:
    return get_user_by_id(user_id)


@app.post("/apiv1/users/")
async def create(user: RequestUser) -> ResponseUser:
    return create_user(user)


# login APIはTodo


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
