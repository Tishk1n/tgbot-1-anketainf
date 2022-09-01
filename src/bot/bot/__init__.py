import logging
from asyncio import new_event_loop, set_event_loop
from os import getenv

from bot.database import init as database_init
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from bot.handlers import register_handlers
from bot.rules import register_rules


def main(token: str):
    _asyncio_database_init()
    bot = Bot(token)
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_rules(dp)
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)


def _asyncio_database_init() -> None:
    loop = new_event_loop()
    set_event_loop(loop)
    db_url = f'mysql://{getenv("MYSQL_USER")}:{getenv("MYSQL_PASSWORD")}@{getenv("MYSQL_HOST")}:{getenv("MYSQL_PORT")}/{getenv("MYSQL_DATABASE")}'
    loop.run_until_complete(database_init(db_url=db_url))
    logging.info('run database')
