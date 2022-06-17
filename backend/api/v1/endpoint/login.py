from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from backend.models import Users
from backend.core import verify_password, create_access_token,settings
from backend.schemas import UserIn_Pydantic, User_Pydantic

user_rl = APIRouter(tags=['认证相关'])


# @user_rl.post("/login", summary="登录")
# async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
#     if user := await Users.get(username=form_data.username):
#         if verify_password(form_data.password, user.password):
#             access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#             access_token = create_access_token(
#                 {"id": user.pk}, expires_delta=access_token_expires
#             )
#
#             return {"access_token": access_token, "token_type": "bearer"}
#     return {"msg": "账户名 或 密码错误"}
# return HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail="Incorrect username or password",
#     headers={"WWW-Authenticate": "Bearer"},
# )


@user_rl.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await Users.get(username=form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="查无此人")
    if verify_password(form_data.password, user.password):
        if verify_password(form_data.password, user.password):
            access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                {"sub": user.username}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer"}
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="验证失败")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")


@user_rl.post("/register", summary="用户新增")
async def register(user: UserIn_Pydantic):
    if await Users.filter(username=user.username):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户已存在.",
        )
    return HTTPException(
        status_code=status.HTTP_201_CREATED,
        detail=await User_Pydantic.from_tortoise_orm(await Users.create(**user.dict()))
    )
