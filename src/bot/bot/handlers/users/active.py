import json
from os import getenv

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from bot.database.models import User
from bot.keyboards.users.finish.inline import finish_keyboard, change_keyboard
from bot.keyboards.users.main.reply import start_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def get_credit_card(message: Message, state: FSMContext):
    await state.update_data(credit_card=message.text)
    if message.text.lower() == "нет":
        await message.answer('Сейчас заполняем раздел Активы, все данные пишите в 1 сообщении!')
        await message.answer('Если у вас в собственности есть автомобиль, укажите:\n'
                             '- Марка и модель\n'
                             '- стоимость\n'
                             '- год выпуска\n'
                             '- находится ли в залоге\n'
                             '(Если автомобиля нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
        await Questionnaire.CAR.set()
    else:
        await message.answer('Напишите, какой месячный лимит каждой карты через запятую (30 тыс., 50 тыс. и т.д.)')
        await Questionnaire.LIMIT.set()


async def get_credit_card_change(message: Message, state: FSMContext):
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.credit_count = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_limit(message: Message, state: FSMContext):
    await state.update_data(limit_card=message.text)
    await message.answer('Сейчас заполняем раздел Активы')
    await message.answer('Если у вас в собственности есть автомобиль, укажите:\n'
                         '- Марка и модель\n'
                         '- стоимость\n'
                         '- год выпуска\n'
                         '- находится ли в залоге\n'
                         '(Если автомобиля нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
    await Questionnaire.CAR.set()


async def get_limit_change(message: Message, state: FSMContext):
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.limit_card = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_car(message: Message, state: FSMContext):
    await state.update_data(car=message.text)
    await message.answer('Если у вас в собственности есть недвижимость укажите:\n'
                         '- тип объекта (квартира, дом, участок …)\n'
                         '- находится ли в залоге\n'
                         '- право возникновения (Покупка, дарение, приватизация, наследство)\n'
                         '- площадь\n'
                         '- размер доли в %\n'
                         '- стоимость\n'
                         '- год приобретения\n'
                         '- адрес объекта\n'
                         '(Если объекта недвижимости нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
    await Questionnaire.PROPERTY.set()


async def get_car_change(message: Message, state: FSMContext):
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.car = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_property(message: Message, state: FSMContext):
    await state.update_data(property=message.text)
    info = await state.get_data()
    await message.answer('Анкета готова', reply_markup=finish_keyboard)
    await message.answer('Анкета отправлена на рассмотрение администраторам', reply_markup=start_keyboard)
    await User(
        id_tg=message.from_id,
        photos=json.dumps(info.get('photos')),
        income=info.get('income'),
        fact_address=info.get('fact_address'),
        time_this=info.get('time_this'),
        address=info.get('address'),
        study=info.get('study'),
        material_status=info.get('material_status'),
        marriage=info.get('marriage'),
        social=info.get('social'),
        email=info.get('email'),
        phone=info.get('phone'),
        snils=info.get('snils'),
        busyness_type=info.get('busyness_type'),
        card_company=info.get('card_company'),
        start_time_work=info.get('start_time_work'),
        full_name=info.get('full_name'),
        address_company=info.get('address_company'),
        site=info.get('site'),
        phone_company=info.get('phone_company'),
        first_work=info.get('first_work'),
        post=info.get('post'),
        main_income=info.get('main_income'),
        back_income=info.get('back_income'),
        credit_count=info.get('credit_count'),
        credit_card=info.get('credit_card'),
        limit_card=info.get('limit_card'),
        car=info.get('car'),
        property=info.get('property'),
    ).save()
    await state.finish()
    await message.bot.send_message(getenv('CHANNEL_ID'), f'Новая анкета от {message.from_id}')


async def get_property_change(message: Message, state: FSMContext):
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.property = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(get_credit_card, state=Questionnaire.CREDIT_CARD)
    dp.register_message_handler(get_credit_card_change, state=Change.CREDIT_CARD)
    dp.register_message_handler(get_limit, state=Questionnaire.LIMIT)
    dp.register_message_handler(get_limit_change, state=Change.LIMIT)
    dp.register_message_handler(get_car, state=Questionnaire.CAR)
    dp.register_message_handler(get_car_change, state=Change.CAR)
    dp.register_message_handler(get_property, state=Questionnaire.PROPERTY)
    dp.register_message_handler(get_property_change, state=Change.PROPERTY)
