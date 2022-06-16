from fastapi import APIRouter



user = APIRouter(tags=['用户相关'])


@user.get("/user",summary="当前用户")
async def current_user():
    return "user_login"

@user.put("/user",summary="修改信息")
async def user_update():
    return "user_login"


# 指定能导出去的包
__all__= [
    "user"
]