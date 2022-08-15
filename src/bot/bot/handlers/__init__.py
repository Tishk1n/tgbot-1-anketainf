from aiogram import Dispatcher

from bot.handlers.users import registers as users_register
from bot.handlers.admins import registers as admins_register


def register_handlers(dp: Dispatcher) -> None:
    users_register(dp)
    admins_register(dp)
