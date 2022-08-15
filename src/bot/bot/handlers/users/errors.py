from aiogram import Dispatcher
from aiogram.types import Update

from bot.errors.error_price import ErrorPrice
from bot.errors.error_wishes import ErrorWishes


async def error_wishes(update: Update, exception: ErrorWishes) -> bool:
    await update.message.answer(exception)
    return True


async def error_price(update: Update, exception: ErrorPrice) -> bool:
    await update.message.answer(exception)
    return True


def register(dp: Dispatcher):
    dp.register_errors_handler(error_wishes, exception=ErrorWishes)
    dp.register_errors_handler(error_price, exception=ErrorPrice)
