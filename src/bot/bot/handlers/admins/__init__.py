from aiogram import Dispatcher
from bot.handlers.admins.main import register as main_register
from bot.handlers.admins.order import register as order_register


def registers(dp: Dispatcher) -> None:
    main_register(dp)
    order_register(dp)

