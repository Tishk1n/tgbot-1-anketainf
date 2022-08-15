from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode, Message

from bot.database.models import User
from bot.keyboards.users.address.inline import address_keyboard
from bot.keyboards.users.busyness_type.inline import busyness_keyboard, card_keyboard
from bot.keyboards.users.finish.inline import change_keyboard
from bot.keyboards.users.income.inline import income_keyboard
from bot.keyboards.users.main.inline import continue_menu
from bot.keyboards.users.marital_status.inline import material_status_keyboard, prenuptial_agreement_keyboard, \
    social_status_keyboard
from bot.keyboards.users.study.inline import study_keyboards
from bot.states.users.change import Change


async def show_questionnaire(call: CallbackQuery, state: FSMContext) -> None:
    user = await User.get(id_tg=call.from_user.id)
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def show_variable(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer("""Выберите пункт
1 - фото паспорта
2 - Способ подтверждения дохода
3 - Адрес фактического проживания
4 - Сколько времени проживаете по этому адресу
5 - Основание проживания
6 - Образование
7 - Семейное положение
8 - Брачный контракт
9 - Социальный статус супруга(-и)
10 - Электронная почта
11 - Номер телефона
12 - Номер СНИЛС
13 - Тип занятости
14 - Карточка компании
15 - Дата начала работы в указанной организации
16 - Полное наименование компании
17 - Фактический адрес компании
18 - Сайт компании
19 - Номер телефона компании
20 - Дата начала своей трудовой деятельности
21 - Название должности
22 - Основной доход в месяц в рублях
23 - Дополнительный доход в месяц
24 - Сумма выплат на  погашение кредитов
25 - Сколько кредитных карт
26 - Месячный лимит каждой карты через запятую
27 - Автомобиль\и
28 - Недвижимость\и
""")
    await Change.change.set()


async def get_variable(message: Message, state: FSMContext) -> None:
    match message.text:
        case '1':
            await message.answer(
                'Загрузите фотографии всех страниц паспорта\n''P.S: Когда загрузите все фото - нажмите кнопку "ЗАКОНЧИЛ"',
                reply_markup=continue_menu
            )
            await Change.PASSPORT.set()
        case '2':
            await message.answer('Выберите способ подтверждения дохода', reply_markup=income_keyboard)
            await Change.INCOME.set()
        case '3':
            await message.answer('Укажите свой адрес фактического проживания:')
            await Change.FACT_ADDRESS.set()
        case '4':
            await message.answer('Сколько времени вы проживаете по этому адресу?')
            await Change.TIME_LIVE_THIS.set()
        case '5':
            await message.answer('Выберите основание проживания', reply_markup=address_keyboard)
            await Change.ADDRESS.set()
        case '6':
            await message.answer('Выберите своё образование', reply_markup=study_keyboards)
            await Change.STUDY.set()
        case '7':
            await message.answer('Выберите семейное положение:', reply_markup=material_status_keyboard)
            await Change.MATERIAL_STATUS.set()
        case '8':
            await message.answer('Брачный контракт', reply_markup=prenuptial_agreement_keyboard)
            await Change.MARRIAGE.set()
        case '9':
            await message.answer('Выберите соц. статус супруга(-и)', reply_markup=social_status_keyboard)
            await Change.SOCIAL.set()
        case '10':
            await message.answer('Укажите свою электронную почту')
            await Change.EMAIL.set()
        case '11':
            await message.answer('Укажите свой номер телефона')
            await Change.PHONE.set()
        case '12':
            await message.answer('Укажите свой снилс')
            await Change.SNILS.set()
        case '13':
            await message.answer('Выберите тип занятости', reply_markup=busyness_keyboard)
            await Change.BUSYNESS_TYPE.set()
        case '14':
            await message.answer('Выберете способ загрузки карточки компании', reply_markup=card_keyboard)
            await Change.CARD_TYPE.set()
        case '15':
            await message.answer('Напишите дату начала работы в указанной компании')
            await Change.BEGIN_WORK.set()
        case '16':
            await message.answer('Укажите полное название компании')
            await Change.FULL_NAME_COMPANY.set()
        case '17':
            await message.answer('Укажите фактический адрес компании')
            await Change.ADDRESS_COMPANY.set()
        case '18':
            await message.answer('Укажите сайт компании')
            await Change.SITE_COMPANY.set()
        case '19':
            await message.answer('Укажите номер телефона компании')
            await Change.PHONE_COMPANY.set()
        case '20':
            await message.answer('Укажите дату начала своей трудовой деятельности')
            await Change.FIRST_WORK.set()
        case '21':
            await message.answer('Укажи название своей должности')
            await Change.POST.set()
        case '22':
            await message.answer('Укажите свой основной доход в месяц в рублях (Пример: 200000 руб.)')
            await Change.MAIN_INCOME.set()
        case '23':
            await message.answer('Укажите свой дополнительный доход в месяц (если его нет, то напишите “нет”)')
            await Change.BACK_INCOME.set()
        case '24':
            await message.answer(
                'Если у вас есть кредиты, напишите сколько в месяц ты выплачиваешь на их погашение (Если кредитов нет, напиши “нет”, если их несколько проссумируй)')
            await Change.CREDIT.set()
        case '25':
            await message.answer(
                'Если у вас есть кредитная карта, укажите сколько их у вас(1, 2, 3, 4)\n(Если карты  нет, напиши “нет”)')
            await Change.CREDIT_CARD.set()
        case '26':
            await message.answer('Напишите, какой месячный лимит каждой карты через запятую (30 тыс., 50 тыс. и т.д.)')
            await Change.LIMIT.set()
        case '27':
            await message.answer('Если у вас в собственности есть автомобиль, укажите:\n'
                                 '- Марка и модель\n'
                                 '- стоимость\n'
                                 '- год выпуска\n'
                                 '- находится ли в залоге\n'
                                 '(Если автомобиля нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
            await Change.CAR.set()
        case '28':
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
            await Change.PROPERTY.set()


def register(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(show_questionnaire, text='fin')
    dp.register_callback_query_handler(show_variable, text='change')
    dp.register_message_handler(get_variable, state=Change.change)