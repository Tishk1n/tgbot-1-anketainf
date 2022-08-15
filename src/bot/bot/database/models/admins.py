"""
    Tortoise model about all administrators project
"""

from tortoise import fields

from bot.database.models.abstract_base import AbstractBaseModel


class Admin(AbstractBaseModel):
    id_tg = fields.IntField(null=False, unique=True)

    class Meta:
        table = "admins"
