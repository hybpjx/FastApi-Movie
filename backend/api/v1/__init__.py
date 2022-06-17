from fastapi import APIRouter
from .endpoint import *

v1 = APIRouter()

v1.include_router(user_rl,prefix="/v1")
v1.include_router(movie,prefix="/v1")
v1.include_router(user,prefix="/v1")