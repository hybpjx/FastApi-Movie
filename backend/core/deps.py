from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from starlette import status
from fastapi.requests import Request

from core import config
from core.security import oauth2_scheme
from models import Users

async def get_current_user(request:Request,token: str = Depends(oauth2_scheme)):
    """
    oauth2_scheme 从请求头中取得Authorization 从而解析token
    :param token: 解析token 获取当前对象
    :return: 当前用户对象
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.core_settings.SECRET_KEY, algorithms=[config.core_settings.ALGORITHM])
        # 字典取值 取值取不到 就返回空
        username: str = payload.get("sub",None)
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    user = await Users.get(username=username)

    # redis 操作
    if await request.state.redis.get(user.username) is None:
        raise HTTPException(detail="数据已经失效",status_code=status.HTTP_408_REQUEST_TIMEOUT)


    if user is None:
        raise credentials_exception
    return user