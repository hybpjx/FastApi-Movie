from tortoise.contrib.pydantic import pydantic_model_creator
from backend.models import Users
User_Pydantic = pydantic_model_creator(Users, name="User", exclude=("password",))
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)

