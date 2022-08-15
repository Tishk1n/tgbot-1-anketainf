from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.keyboards.users.main.inline import begin_get_quests_keyboard
from bot.keyboards.users.main.reply import start_keyboard, start_button, cancel_button


async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.finish()
    await message.answer("Привет!", reply_markup=start_keyboard)


async def btn_first_message(message: Message, state: FSMContext):
    await state.finish()
    msg = 'Привет! Я помощник Лилии, задам тебе несколько вопросов, чтобы заполнить твою анкету клиента.'
    await message.answer(msg, reply_markup=begin_get_quests_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands='start', state='*')
    dp.register_message_handler(btn_first_message, text=start_button[0])
    dp.register_message_handler(btn_first_message, text=cancel_button[0], state='*')
