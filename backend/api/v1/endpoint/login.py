from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from backend.models import Users
from backend.core import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from backend.schemas import UserIn_Pydantic

user_rl = APIRouter(tags=['认证相关'])


@user_rl.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if user := await Users.get(username=form_data.username):
        if verify_password(form_data.password, user.password):
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"id": user.pk}, expires_delta=access_token_expires
            )

            return {"access_token": access_token, "token_type": "bearer"}

    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@user_rl.post("/register", summary="用户新增")
async def register(user: UserIn_Pydantic):
    db_user = await Users.create(**user.dict())
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_user
