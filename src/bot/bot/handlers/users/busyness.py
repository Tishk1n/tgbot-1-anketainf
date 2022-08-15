from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ParseMode

from bot.database.models import User
from bot.keyboards.users.busyness_type.inline import busyness_keyboard, card_keyboard
from bot.keyboards.users.finish.inline import change_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def start_busyness(message: Message, state: FSMContext):
    await state.update_data(snils=message.text)
    await message.answer('Сейчас заполняем раздел Занятость')
    await message.answer('Выберите тип занятости', reply_markup=busyness_keyboard)
    await Questionnaire.BUSYNESS_TYPE.set()


async def start_busyness_change(message: Message, state: FSMContext):
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.snils = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_busyness_type(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'kom':
            variable = "Коммерческая"
        case 'byd':
            variable = "Бюджетная"
        case 'cdoy_buz':
            variable = "Свой бизнес"
        case 'naym':
            variable = "По найму"
        case 'pencioner':
            variable = "Пенсионер"
        case _:
            variable = "ИП"
    await state.update_data(busyness_type=variable)
    await call.message.answer('Выберете способ загрузки карточки компании', reply_markup=card_keyboard)
    await Questionnaire.CARD_TYPE.set()


async def get_busyness_type_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'kom':
            variable = "Коммерческая"
        case 'byd':
            variable = "Бюджетная"
        case 'cdoy_buz':
            variable = "Свой бизнес"
        case 'naym':
            variable = "По найму"
        case 'pencioner':
            variable = "Пенсионер"
        case _:
            variable = "ИП"
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.busyness_type = variable
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_type_card(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'upload':
            await call.message.answer('Загрузите карточку')
            await Questionnaire.CARD_UPLOAD.set()
        case _:
            await call.message.answer('1) Укажите полное наименование компании\n'
                                      '2) Укажите фактический адрес компании\n'
                                      '3) Укажите сайт компании\n'
                                      '4) Напишите номер телефона компании\n'
                                      '(Все вводите в 1 сообщении)')
            await Questionnaire.CARD_MYSELF.set()


async def get_type_card_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'upload':
            await call.message.answer('Загрузите карточку')
            await Change.CARD_UPLOAD.set()
        case _:
            await call.message.answer('1) Укажите полное наименование компании\n'
                                      '2) Укажите фактический адрес компании\n'
                                      '3) Укажите сайт компании\n'
                                      '4) Напишите номер телефона компании\n'
                                      '(Все вводите в 1 сообщении)')
            await Change.CARD_MYSELF.set()


async def get_card_document(message: Message, state: FSMContext) -> None:
    await state.update_data(card_company=await message.document.get_url())
    await message.answer('Напишите дату начала работы в указанной компании')
    await Questionnaire.BEGIN_WORK.set()


async def get_card_document_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.card_company = await message.document.get_url()
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_card_photo(message: Message, state: FSMContext) -> None:
    await state.update_data(card_company=await message.photo[-1].get_url())
    await message.answer('Напишите дату начала работы в указанной компании')
    await Questionnaire.BEGIN_WORK.set()


async def get_card_photo_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.card_company = await message.photo[-1].get_url()
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_card(message: Message, state: FSMContext) -> None:
    await state.update_data(card_company=message.text)
    await message.answer('Напишите дату начала работы в указанной компании')
    await Questionnaire.BEGIN_WORK.set()


async def get_card_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.card_company = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_start_time_work(message: Message, state: FSMContext) -> None:
    await state.update_data(start_time_work=message.text)
    await message.answer('Укажите полное название компании')
    await Questionnaire.FULL_NAME_COMPANY.set()


async def get_start_time_work_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.start_time_work = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_full_name(message: Message, state: FSMContext) -> None:
    await state.update_data(full_name=message.text)
    await message.answer('Укажите фактический адрес компании')
    await Questionnaire.ADDRESS_COMPANY.set()


async def get_full_name_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.full_name = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_address_company(message: Message, state: FSMContext) -> None:
    await state.update_data(address_company=message.text)
    await message.answer('Укажите сайт компании')
    await Questionnaire.SITE_COMPANY.set()


async def get_address_company_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.address_company = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_site(message: Message, state: FSMContext) -> None:
    await state.update_data(site=message.text)
    await message.answer('Укажите номер телефона компании')
    await Questionnaire.PHONE_COMPANY.set()


async def get_site_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.site = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_phone_company(message: Message, state: FSMContext) -> None:
    await state.update_data(phone_company=message.text)
    await message.answer('Укажите дату начала своей трудовой деятельности')
    await Questionnaire.FIRST_WORK.set()


async def get_phone_company_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.phone_company = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_time_first_work(message: Message, state: FSMContext) -> None:
    await state.update_data(first_work=message.text)
    await message.answer('Укажи название своей должности')
    await Questionnaire.POST.set()


async def get_time_first_work_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.first_work = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher):
    dp.register_message_handler(start_busyness, state=Questionnaire.SNILS)
    dp.register_message_handler(start_busyness_change, state=Change.SNILS)
    dp.register_callback_query_handler(get_busyness_type, state=Questionnaire.BUSYNESS_TYPE)
    dp.register_callback_query_handler(get_busyness_type_change, state=Change.BUSYNESS_TYPE)
    dp.register_callback_query_handler(get_type_card, state=Questionnaire.CARD_TYPE)
    dp.register_callback_query_handler(get_type_card_change, state=Change.CARD_TYPE)
    dp.register_message_handler(get_card_document, content_types='document', state=Questionnaire.CARD_UPLOAD)
    dp.register_message_handler(get_card_document_change, content_types='document', state=Change.CARD_UPLOAD)
    dp.register_message_handler(get_card_photo, content_types='photo', state=Questionnaire.CARD_UPLOAD)
    dp.register_message_handler(get_card_photo_change, content_types='photo', state=Change.CARD_UPLOAD)
    dp.register_message_handler(get_card, state=Questionnaire.CARD_MYSELF)
    dp.register_message_handler(get_card_change, state=Change.CARD_MYSELF)
    dp.register_message_handler(get_start_time_work, state=Questionnaire.BEGIN_WORK)
    dp.register_message_handler(get_start_time_work_change, state=Change.BEGIN_WORK)
    dp.register_message_handler(get_full_name, state=Questionnaire.FULL_NAME_COMPANY)
    dp.register_message_handler(get_full_name_change, state=Change.FULL_NAME_COMPANY)
    dp.register_message_handler(get_address_company, state=Questionnaire.ADDRESS_COMPANY)
    dp.register_message_handler(get_address_company_change, state=Change.ADDRESS_COMPANY)
    dp.register_message_handler(get_site, state=Questionnaire.SITE_COMPANY)
    dp.register_message_handler(get_site_change, state=Change.SITE_COMPANY)
    dp.register_message_handler(get_phone_company, state=Questionnaire.PHONE_COMPANY)
    dp.register_message_handler(get_phone_company_change, state=Change.PHONE_COMPANY)
    dp.register_message_handler(get_time_first_work, state=Questionnaire.FIRST_WORK)
    dp.register_message_handler(get_time_first_work_change, state=Change.FIRST_WORK)
