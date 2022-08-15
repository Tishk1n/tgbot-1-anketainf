from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from bot.database.models import User
from bot.keyboards.users.finish.inline import change_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def get_email(message: Message, state: FSMContext) -> None:
    await state.update_data(email=message.text)
    await message.answer('Укажите свой номер телефона')
    await Questionnaire.PHONE.set()


async def get_email_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.email = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_phone(message: Message, state: FSMContext) -> None:
    await state.update_data(phone=message.text)
    await message.answer('Укажите свой снилс')
    await Questionnaire.SNILS.set()


async def get_phone_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.phone = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(get_email, state=Questionnaire.EMAIL)
    dp.register_message_handler(get_email_change, state=Change.EMAIL)
    dp.register_message_handler(get_phone, state=Questionnaire.PHONE)
    dp.register_message_handler(get_phone_change, state=Change.PHONE)
