from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode

from bot.database.models import User
from bot.keyboards.users.finish.inline import change_keyboard
from bot.keyboards.users.marital_status.inline import material_status_keyboard
from bot.states.users.change import Change
from bot.states.users.questionnaire import Questionnaire


async def get_study(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'uc':
            variable = "Ученая степень"
        case '2v':
            variable = "Два высших и более"
        case 'vuc':
            variable = "Высшее"
        case 'nv':
            variable = "Неоконченное высшее"
        case 'cz':
            variable = "Среднее специальное"
        case 'cr':
            variable = "Среднее"
        case 'nuvc':
            variable = "Ниже среднего"
        case 'rm':
            variable = "Российское МВА"
        case _:
            variable = "Иностранное МВА"
    await state.update_data(study=variable)
    await call.message.answer('Выберите семейное положение:', reply_markup=material_status_keyboard)
    await Questionnaire.MATERIAL_STATUS.set()


async def get_study_change(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'uc':
            variable = "Ученая степень"
        case '2v':
            variable = "Два высших и более"
        case 'vuc':
            variable = "Высшее"
        case 'nv':
            variable = "Неоконченное высшее"
        case 'cz':
            variable = "Среднее специальное"
        case 'cr':
            variable = "Среднее"
        case 'nuvc':
            variable = "Ниже среднего"
        case 'rm':
            variable = "Российское МВА"
        case _:
            variable = "Иностранное МВА"
    await state.finish()
    user = await User.get(id_tg=call.from_user.id)
    user.study = variable
    await user.save()
    await call.message.answer(user.to_str(), parse_mode=ParseMode.HTML, reply_markup=change_keyboard)


def register(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(get_study, state=Questionnaire.STUDY)
    dp.register_callback_query_handler(get_study_change, state=Change.STUDY)
