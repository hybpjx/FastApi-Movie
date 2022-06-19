from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    SUCCESS: int = 200
    CREATED: int = 201
    NOT_FOUND: int = 404
    BAD_REQUEST: int = 400
    UNAUTHORIZED: int = 401


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="业务状态码")
    data: Any = Field(default="", description="数据结果")
    msg: str = Field(default="", description="自定义数据")


class ResponseToken(ResponseBasic):
    access_token: Optional[str]
    token_type: Optional[str] = Field(default="bearer")


class Response200(ResponseBasic):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="请求成功")


class Response201(ResponseBasic):
    code: CodeEnum = Field(default=CodeEnum.CREATED, description="成功创建资源")


class Response400(ResponseBasic):
    code: CodeEnum = CodeEnum.BAD_REQUEST
    msg: str = "无法解析该请求。"


class Response401(ResponseBasic):
    code: CodeEnum = CodeEnum.UNAUTHORIZED
    msg: str = "请求没有进行身份验证或验证未通过。"


class Response404(ResponseBasic):
    code: CodeEnum = CodeEnum.NOT_FOUND
    msg: str = "找不到请求。"
