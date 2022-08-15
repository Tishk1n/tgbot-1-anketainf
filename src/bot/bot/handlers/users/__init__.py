from aiogram import Dispatcher
from bot.handlers.users.main import register as main_register
from bot.handlers.users.passport import register as passport_register
from bot.handlers.users.income import register as income_register
from bot.handlers.users.address import register as address_register
from bot.handlers.users.study import register as study_register
from bot.handlers.users.material_status import register as material_register
from bot.handlers.users.contact_info import register as contact_register
from bot.handlers.users.busyness import register as busyness_register
from bot.handlers.users.finance import register as finance_register
from bot.handlers.users.active import register as active_register
from bot.handlers.users.finish import register as finish_register


def registers(dp: Dispatcher) -> None:
    main_register(dp)
    passport_register(dp)
    income_register(dp)
    address_register(dp)
    study_register(dp)
    material_register(dp)
    contact_register(dp)
    busyness_register(dp)
    finance_register(dp)
    active_register(dp)
    finish_register(dp)
