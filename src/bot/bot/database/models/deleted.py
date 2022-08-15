from tortoise import fields

from bot.database.models.abstract_base import AbstractBaseModel


class Deleted(AbstractBaseModel):
    id_tg = fields.IntField(null=False, unique=True)

    class Meta:
        table = "deleted"
