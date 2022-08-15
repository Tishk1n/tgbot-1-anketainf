from os import getenv

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, Update


class UserRules(BoundFilter):
    key = 'is_user'

    def __init__(self, is_user):
        self.is_user = is_user
        self.admin_chat = int(getenv('GROUP_ID'))

    async def check(self, update, state: FSMContext = None):
        if isinstance(update, Message):
            return update.chat.id != self.admin_chat
        if isinstance(update, (CallbackQuery, Update)):
            return update.message.chat.id != self.admin_chat
