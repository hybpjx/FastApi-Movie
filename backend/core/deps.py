from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from starlette import status

from backend.core import settings
from backend.core.security import oauth2_scheme
from backend.models import Users

async def get_current_user(token: str = Depends(oauth2_scheme)):
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
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        # 字典取值 取值取不到 就返回空
        username: str = payload.get("sub",None)
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    user = await Users.get(username=username)
    if user is None:
        raise credentials_exception
    return user