from aiogram import Dispatcher

from bot.handlers.admins.main import register as main_register


def registers(dp: Dispatcher) -> None:
    main_register(dp)
