from fastapi import APIRouter
from .endpoint import *

v1 = APIRouter()

v1.include_router(login)
v1.include_router(movie)
v1.include_router(user)