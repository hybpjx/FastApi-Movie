from fastapi import APIRouter, Depends, HTTPException


from core import deps
from models import Users
from schemas import (
    UserIn_Pydantic,
    User_Pydantic,
    Response200,
    Response404,
)

user = APIRouter(tags=['用户相关'], dependencies=[Depends(deps.get_current_user)])


@user.get("/user", summary="当前用户")
async def current_user(user_obj: Users = Depends(deps.get_current_user)):
    return await User_Pydantic.from_tortoise_orm(user_obj)


@user.put("/user", summary="修改信息")
async def user_update(user_form: UserIn_Pydantic, user_obj: Users = Depends(deps.get_current_user)):
    """
    修改当前用户信息
    """
    user_form.username = user_obj.username
    user_form.password = user_obj.password
    if await Users.filter(username=user_obj.username).update(**user_form.dict()):
        return Response200(data=await User_Pydantic.from_tortoise_orm(user_obj))
    return Response404(msg="更新失败")


# async def user_update(user_form: UserIn_Pydantic, user_obj: Users = Depends(deps.get_current_user)):
#     """
#     修改当前用户信息
#     """
#     user_form.username = user_obj.username
#     user_form.password = user_obj.password
#     if await Users.filter(username=user_obj.username).update(**user_form.dict()):
#         return HTTPException(status_code=200, detail=await User_Pydantic.from_tortoise_orm(user_obj))
#     return HTTPException(status_code=404, detail="更新失败")



# 指定能导出去的包
__all__ = [
    "user"
]
