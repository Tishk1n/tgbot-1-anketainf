from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode

from bot.database.models import User
from bot.keyboards.users.finish.inline import change_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def get_income_proof(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'ndfl':
            variable = "2-НДФЛ"
        case 'pfr':
            variable = "Выписка из ПФР"
        case 'nd':
            variable = "Налоговая декларация"
        case 'srp':
            variable = "Справка о размере пенсии"
        case 'spfb':
            variable = "Справка по форме банка"
        case 'vph':
            variable = "Выписка из похозяйственной книги"
        case _:
            variable = "Без подтверждения"
    await state.update_data(income=variable)
    await call.message.answer('Укажите свой адрес фактического проживания:')
    await Questionnaire.FACT_ADDRESS.set()


async def get_income_proof_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'ndfl':
            variable = "2-НДФЛ"
        case 'pfr':
            variable = "Выписка из ПФР"
        case 'nd':
            variable = "Налоговая декларация"
        case 'srp':
            variable = "Справка о размере пенсии"
        case 'spfb':
            variable = "Справка по форме банка"
        case 'vph':
            variable = "Выписка из похозяйственной книги"
        case _:
            variable = "Без подтверждения"
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.income = variable
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(get_income_proof, state=Questionnaire.INCOME)
    dp.register_callback_query_handler(get_income_proof_change, state=Change.INCOME)
