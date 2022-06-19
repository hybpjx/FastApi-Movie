from datetime import timedelta, datetime
from typing import Union


from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from core import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


def get_password_hash(password: str):
    """
    加密密码
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码  hash密码
    :param plain_password:
    :param hashed_password:
    :return:
    """

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    生成token
    :param data:
    :param expires_delta: 有效时间
    :return:
    """
    to_encode = data.copy()
    if expires_delta:
        # 如果传了则 当前时间+ 设置的时间
        expire = datetime.utcnow() + expires_delta
    else:
        # 如果没传 +15 分钟
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.core_settings.SECRET_KEY, algorithm=config.core_settings.ALGORITHM)
    return encoded_jwt



