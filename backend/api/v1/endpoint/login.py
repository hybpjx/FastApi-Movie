from fastapi import APIRouter

login = APIRouter(tags=['认证相关'])


@login.post("/login",summary="登录")
async def user_login():
    return "user_login"