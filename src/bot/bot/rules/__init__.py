from aiogram import Dispatcher

from bot.rules.admins import AdminRules, ReplyRules, FullAdmin
from bot.rules.users import UserRules


def register_rules(dp: Dispatcher):
    dp.filters_factory.bind(AdminRules)
    dp.filters_factory.bind(ReplyRules)
    dp.filters_factory.bind(FullAdmin)
    dp.filters_factory.bind(FullAdmin)
    dp.filters_factory.bind(UserRules)
