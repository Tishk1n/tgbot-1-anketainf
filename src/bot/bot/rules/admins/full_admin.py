from os import getenv

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, Update


class FullAdmin(BoundFilter):
    key = 'is_full_admin'

    def __init__(self, is_full_admin):
        self.is_full_admin = is_full_admin
        self.admin_chat = int(getenv('GROUP_ID'))
        self.admins = [1678937897, 1235766234]

    async def check(self, update, state: FSMContext = None):
        if isinstance(update, Message):
            return update.chat.id == self.admin_chat and update.from_id in self.admins
        if isinstance(update, (CallbackQuery, Update)):
            return update.message.chat.id == self.admin_chat and update.message.from_id in self.admins
