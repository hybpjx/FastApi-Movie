import sys
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import FastAPI, applications
from tortoise.contrib.fastapi import register_tortoise

from .v1 import v1
from backend.core.config import settings

app = FastAPI(
    description=settings.DESC,
    title=settings.TITLE,
)

app.include_router(v1, prefix="/api")

# 解决swagger文档加载不出来的问题
def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url='https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui-bundle.js',
        swagger_css_url='https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.css'
    )


applications.get_swagger_ui_html = swagger_monkey_patch


import logging

fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(fmt)

# will print debug sql
logger_db_client = logging.getLogger("tortoise.db_client")
logger_db_client.setLevel(logging.DEBUG)
logger_db_client.addHandler(sh)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(sh)

register_tortoise(
    app,  # fastapi 的实例
    db_url="sqlite://watch.sqlite",  # 数据库
    modules={"models": ["backend.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
