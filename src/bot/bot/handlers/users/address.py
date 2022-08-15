from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ParseMode

from bot.database.models import User
from bot.keyboards.users.address.inline import address_keyboard
from bot.keyboards.users.finish.inline import change_keyboard
from bot.keyboards.users.study.inline import study_keyboards
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def get_fact_address(message: Message, state: FSMContext) -> None:
    await state.update_data(fact_address=message.text)
    await message.answer('Сколько времени вы проживаете по этому адресу?')
    await Questionnaire.TIME_LIVE_THIS.set()


async def get_fact_address_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.fact_address = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_time_live_this(message: Message, state: FSMContext) -> None:
    await state.update_data(time_this=message.text)
    await message.answer('Выберите основание проживания', reply_markup=address_keyboard)
    await Questionnaire.ADDRESS.set()


async def get_time_live_this_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.time_this = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_address(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'cob':
            variable = "Собственность"
        case 'coz':
            variable = "Социальный найм"
        case 'are':
            variable = "Аренда"
        case 'voi':
            variable = "Воинская часть"
        case 'jr':
            variable = "Жильё родственников"
        case _:
            variable = "Коммунальная квартира"
    await state.update_data(address=variable)
    await call.message.answer('Выберите своё образование', reply_markup=study_keyboards)
    await Questionnaire.STUDY.set()


async def get_address_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'cob':
            variable = "Собственность"
        case 'coz':
            variable = "Социальный найм"
        case 'are':
            variable = "Аренда"
        case 'voi':
            variable = "Воинская часть"
        case 'jr':
            variable = "Жильё родственников"
        case _:
            variable = "Коммунальная квартира"
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.time_this = variable
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(get_fact_address, state=Questionnaire.FACT_ADDRESS)
    dp.register_message_handler(get_fact_address_change, state=Change.FACT_ADDRESS)
    dp.register_message_handler(get_time_live_this, state=Questionnaire.TIME_LIVE_THIS)
    dp.register_message_handler(get_time_live_this_change, state=Change.TIME_LIVE_THIS)
    dp.register_callback_query_handler(get_address, state=Questionnaire.ADDRESS)
    dp.register_callback_query_handler(get_address_change, state=Change.ADDRESS)
