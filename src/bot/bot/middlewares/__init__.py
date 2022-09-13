from aiogram import Dispatcher

from bot.middlewares.album import AlbumMiddleware


def register_middlewares(dp: Dispatcher) -> None:
    dp.middleware.setup(AlbumMiddleware())
