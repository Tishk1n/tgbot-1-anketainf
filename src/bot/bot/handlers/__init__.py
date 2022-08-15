from aiogram import Dispatcher
from bot.handlers.users import registers as users_registers
from bot.handlers.admins import registers as admins_registers


def registers(dp: Dispatcher):
    admins_registers(dp)
    users_registers(dp)
