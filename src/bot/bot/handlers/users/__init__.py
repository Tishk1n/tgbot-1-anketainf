from aiogram import Dispatcher
from bot.handlers.users.main import register as main_register
from bot.handlers.users.scope import register as scope_register
from bot.handlers.users.errors import register as errors_register


def registers(dp: Dispatcher):
    main_register(dp)
    scope_register(dp)
    errors_register(dp)
