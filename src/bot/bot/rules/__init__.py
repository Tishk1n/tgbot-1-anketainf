from aiogram import Dispatcher

from bot.rules.admins import AdminRules


def register_rules(dp: Dispatcher):
    dp.filters_factory.bind(AdminRules)
