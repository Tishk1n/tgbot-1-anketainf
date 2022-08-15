from os import getenv

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class ReplyRules(BoundFilter):
    key = 'is_reply'

    def __init__(self, is_reply):
        self.is_reply = is_reply
        self.admin_chat = int(getenv('GROUP_ID'))

    async def check(self, update: Message, state: FSMContext = None):
        return bool(update.reply_to_message)
