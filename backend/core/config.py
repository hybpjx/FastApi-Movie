from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE: Optional[str] = "电影列表接口"

    DESC: Optional[str] = """
    - 基于 flask电影文档 改写的fastapi小项目
    - tortoise —— fastapi 等
    """

    # JWT 安全配置项目
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3


settings = Settings()
