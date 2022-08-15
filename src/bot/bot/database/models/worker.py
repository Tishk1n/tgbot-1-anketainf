from tortoise import fields

from bot.database.models.abstract_base import AbstractBaseModel


class Worker(AbstractBaseModel):
    username = fields.CharField(max_length=100, null=False, unique=True)
    category = fields.CharField(max_length=1000, null=False)
    stack = fields.CharField(max_length=1000, null=False)

    def to_str(self) -> str:
        return f'<b>{self.username}:</b>\n{self.category}\n{self.stack}'
