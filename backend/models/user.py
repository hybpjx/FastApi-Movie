from typing import Optional, Iterable

from tortoise import fields, models, BaseDBAsyncClient
from backend.core import get_password_hash

class Users(models.Model):
    """
    The User model
    """
    username = fields.CharField(max_length=20, unique=False, description="账号")
    password = fields.CharField(max_length=128, null=False, description="密码")
    nick_name = fields.CharField(max_length=20, null=True, description="昵称", default="过路人")

    async def save(
            self,
            using_db: Optional[BaseDBAsyncClient] = None,
            update_fields: Optional[Iterable[str]] = None,
            force_create: bool = False,
            force_update: bool = False,
    ) -> None:
        await super(Users, self).save(using_db, update_fields, force_create, force_update)
        if force_create or "password" in update_fields:
            self.password = get_password_hash(password=self.password)

