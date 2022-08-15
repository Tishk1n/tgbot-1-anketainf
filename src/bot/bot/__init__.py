from asyncio import new_event_loop, set_event_loop, get_event_loop
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.database import init as database_init
from aiogram.utils import executor

from bot import handlers
from bot.rules import register_rules


def main(token: str) -> None:
    _asyncio_database_init(getenv("MYSQL_USER"), getenv("MYSQL_PASSWORD"), getenv("MYSQL_HOST"), getenv("MYSQL_DATABASE"))
    bot: Bot = Bot(token=token)
    dp: Dispatcher = Dispatcher(bot, loop=get_event_loop(), storage=MemoryStorage())
    register_rules(dp)
    handlers.registers(dp)
    executor.start_polling(dp, skip_updates=True)


def _asyncio_database_init(user, password, host, database) -> None:
    loop = new_event_loop()
    set_event_loop(loop)
    db_url = f'mysql://{user}:{password}@{host}/{database}'
    loop.run_until_complete(database_init(db_url=db_url))
