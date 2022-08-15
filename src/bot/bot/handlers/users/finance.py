from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from bot.database.models import User
from bot.keyboards.users.finish.inline import change_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def begin_finance_quests(message: Message, state: FSMContext) -> None:
    await state.update_data(post=message.text)
    await message.answer('Сейчас заполняем раздел финансов')
    await message.answer('Укажите свой основной доход в месяц в рублях (Пример: 200000 руб.)')
    await Questionnaire.MAIN_INCOME.set()


async def begin_finance_quests_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.post = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_main_income(message: Message, state: FSMContext) -> None:
    await state.update_data(main_income=message.text)
    await message.answer('Укажите свой дополнительный доход в месяц (если его нет, то напишите “нет”)')
    await Questionnaire.BACK_INCOME.set()


async def get_main_income_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.main_income = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_back_income(message: Message, state: FSMContext) -> None:
    await state.update_data(back_income=message.text)
    await message.answer(
        'Если у вас есть кредиты, напишите сколько в месяц ты выплачиваешь на их погашение (Если кредитов нет, напиши “нет”, если их несколько проссумируй)')
    await Questionnaire.CREDIT.set()


async def get_back_income_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.back_income = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


async def get_credit(message: Message, state: FSMContext) -> None:
    await state.update_data(credit_count=message.text)
    await message.answer('Если у вас есть кредитная карта, укажите сколько их у вас(1, 2, 3, 4)\n(Если карты  нет, напиши “нет”)')
    await Questionnaire.CREDIT_CARD.set()


async def get_credit_change(message: Message, state: FSMContext) -> None:
    await state.finish()
    user = await User.get(id_tg=message.from_user.id)
    user.credit_count = message.text
    await user.save()
    await message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(begin_finance_quests, state=Questionnaire.POST)
    dp.register_message_handler(begin_finance_quests_change, state=Change.POST)
    dp.register_message_handler(get_main_income, state=Questionnaire.MAIN_INCOME)
    dp.register_message_handler(get_main_income_change, state=Change.MAIN_INCOME)
    dp.register_message_handler(get_back_income, state=Questionnaire.BACK_INCOME)
    dp.register_message_handler(get_back_income_change, state=Change.BACK_INCOME)
    dp.register_message_handler(get_credit, state=Questionnaire.CREDIT)
    dp.register_message_handler(get_credit_change, state=Change.CREDIT)
