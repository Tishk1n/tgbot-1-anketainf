from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.keyboards.users.main.reply import main_keyboard, main_button, scope_keyboard, scope_button


async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.finish()
    await message.answer("Загрузка меню...", reply_markup=main_keyboard)


async def bnt_choice_scope(message: Message, state: FSMContext) -> None:
    await state.finish()
    await message.answer("Привет! Выбери сферу для заказа:", reply_markup=scope_keyboard)


def register(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start', state='*', is_user=True)
    dp.register_message_handler(cmd_start, text=scope_button[-1], state='*', is_user=True)
    dp.register_message_handler(bnt_choice_scope, text=[main_button[0]], is_user=True)
