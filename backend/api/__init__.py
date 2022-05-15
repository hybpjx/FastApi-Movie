from fastapi import FastAPI
from .v1 import v1

app = FastAPI()

app.include_router(v1, prefix="/api")
