"""
    Abstract Tortoise base model with default primary key ID.
"""

from tortoise import fields
from tortoise.models import Model


class AbstractBaseModel(Model):
    """
    Encapsulates realisation of the ID field.
    """

    id = fields.IntField(pk=True)

    class Meta:
        abstract = True
