import asyncio

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ParseMode

from bot.database.models import User
from bot.database.models.deleted import Deleted
from bot.keyboards.users.finish.inline import change_keyboard
from bot.keyboards.users.income.inline import income_keyboard
from bot.keyboards.users.main.inline import continue_menu
from bot.keyboards.users.main.reply import cancel_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def begin_write_questionnaire(call: CallbackQuery, state: FSMContext) -> None:
    if await Deleted.filter(id_tg=call.from_user.id).exists():
        await call.message.answer('Ваша анкета была отклонена без возможности исправления')
        return
    if not await User.filter(id_tg=call.from_user.id).exists():
        await call.message.answer('Сейчас заполняем раздел "Личная информация"', reply_markup=cancel_keyboard)
        await call.message.answer(
            'Загрузите фотографии всех страниц паспорта\n''P.S: Когда загрузите все фото - нажмите кнопку "ЗАКОНЧИЛ"',
            reply_markup=continue_menu
        )
        await Questionnaire.PASSPORT.set()
        return
    await call.message.answer('Вы уже заполнили свою анкету')


async def get_photo_passport(message: Message, state: FSMContext) -> None:
    info = await state.get_data()
    photos: list[str] = info['photos'] if info.get('photos') else []
    url: str = await message.photo[-1].get_url()
    photos.append(url)
    await state.update_data(photos=photos)
    await message.answer('Фото сохранено')


async def error_photo(message: Message, state: FSMContext) -> None:
    await message.answer('Ошибка файла, пришлите фото')


async def begin_income(call: CallbackQuery, state: FSMContext) -> None:
    info = await state.get_data()
    if not info.get('photos'):
        await call.message.answer('Необходимо добавить фото!')
        return
    await call.message.answer('Выберите способ подтверждения дохода', reply_markup=income_keyboard)
    await Questionnaire.INCOME.set()


async def end_change(call: CallbackQuery, state: FSMContext) -> None:
    info = await state.get_data()
    if not info.get('photos'):
        await call.message.answer('Необходимо добавить фото!')
        return
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.photos = info['photos']
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(begin_write_questionnaire, text='begin_quest')
    dp.register_callback_query_handler(begin_income, text='end', state=Questionnaire.PASSPORT)
    dp.register_callback_query_handler(end_change, text='end', state=Change.PASSPORT)
    dp.register_message_handler(get_photo_passport, content_types='photo', state=Questionnaire.PASSPORT)
    dp.register_message_handler(get_photo_passport, content_types='photo', state=Change.PASSPORT)
    dp.register_message_handler(error_photo, content_types=['text', 'document'], state=Questionnaire.PASSPORT)
    dp.register_message_handler(error_photo, content_types=['text', 'document'], state=Change.PASSPORT)
