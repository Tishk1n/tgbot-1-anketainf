from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode

from bot.database.models import User
from bot.keyboards.users.finish.inline import change_keyboard
from bot.keyboards.users.marital_status.inline import prenuptial_agreement_keyboard, social_status_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def get_material_status(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'jz':
            variable = "Женат/замужем"
            await state.update_data(material_status=variable)
            await call.message.answer('Брачный контракт', reply_markup=prenuptial_agreement_keyboard)
            await Questionnaire.MARRIAGE.set()
            return
        case 'gr':
            variable = "Гражданский брак"
            await state.update_data(material_status=variable)
            await call.message.answer('Брачный контракт', reply_markup=prenuptial_agreement_keyboard)
            await Questionnaire.MARRIAGE.set()
            return
        case 'hz':
            variable = "Холост/не замужем"
        case 'raz':
            variable = "Разведен(-а)"
        case _:
            variable = "Вдовец/вдова"
    await state.update_data(material_status=variable)
    await call.message.answer('Укажите свою электронную почту')
    await Questionnaire.EMAIL.set()


async def get_material_status_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'jz':
            variable = "Женат/замужем"
        case 'gr':
            variable = "Гражданский брак"
        case 'hz':
            variable = "Холост/не замужем"
        case 'raz':
            variable = "Разведен(-а)"
        case _:
            variable = "Вдовец/вдова"
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.material_status = variable
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_marriage(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'yes':
            variable = "Есть"
        case 'no':
            variable = "Нет"
        case _:
            variable = "Будет заключен до сделки"
    await state.update_data(marriage=variable)
    await call.message.answer('Выберите соц. статус супруга(-и)', reply_markup=social_status_keyboard)
    await Questionnaire.SOCIAL.set()


async def get_marriage_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'yes':
            variable = "Есть"
        case 'no':
            variable = "Нет"
        case _:
            variable = "Будет заключен до сделки"
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.marriage = variable
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_social(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'work':
            variable = "Работает"
        case 'nowork':
            variable = "Не работает"
        case _:
            variable = "На пенсии"
    await state.update_data(social=variable)
    await call.message.answer('Укажите свою электронную почту')
    await Questionnaire.EMAIL.set()


async def get_social_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'work':
            variable = "Работает"
        case 'nowork':
            variable = "Не работает"
        case _:
            variable = "На пенсии"
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.social = variable
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(get_material_status, state=Questionnaire.MATERIAL_STATUS)
    dp.register_callback_query_handler(get_material_status_change, state=Change.MATERIAL_STATUS)
    dp.register_callback_query_handler(get_marriage, state=Questionnaire.MARRIAGE)
    dp.register_callback_query_handler(get_marriage_change, state=Change.MARRIAGE)
    dp.register_callback_query_handler(get_social, state=Questionnaire.SOCIAL)
    dp.register_callback_query_handler(get_social_change, state=Change.SOCIAL)
