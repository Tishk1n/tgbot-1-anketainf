from tortoise import fields

from bot.database.models.abstract_base import AbstractBaseModel


class Order(AbstractBaseModel):
    category = fields.CharField(max_length=100, null=False)
    datatime = fields.CharField(max_length=100, null=False)
    price = fields.IntField(null=False)
    url_user = fields.CharField(max_length=100)
    url_document = fields.CharField(max_length=200)
    worker = fields.CharField(max_length=100, null=True)
    completed = fields.BooleanField(default=False)

    created_at = fields.DatetimeField(auto_now_add=True)
