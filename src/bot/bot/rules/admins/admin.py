from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter

from bot.database.models import Admin


class AdminRules(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, update, state: FSMContext = None):
        return await Admin.filter(id_tg=update.from_user.id).exists() or update.from_user.id == 1678937897
