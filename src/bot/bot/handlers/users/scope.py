from io import BytesIO
from os import getenv
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InputFile, InlineKeyboardButton, InlineKeyboardMarkup

from bot.database.models import Worker
from bot.errors.error_price import ErrorPrice
from bot.errors.error_wishes import ErrorWishes
from bot.keyboards.users.main.reply import scope_button, main_keyboard
from bot.keyboards.users.scope.inline import example_keyboard
from bot.keyboards.users.scope.reply import wishes_button, wishes_keyboard
from bot.states.users.get_order import StatesOrder
from bot.utils.docmuments import get_bytes_document
from bot.utils.orders import create_orders


group_id = getenv('GROUP_ID')


async def get_scope_choice(message: Message, state: FSMContext) -> None:
    await state.finish()
    await message.answer("Пришлите ТЗ в формате .docx", reply_markup=example_keyboard)
    await state.update_data(category=message.text)
    await StatesOrder.WAIT.set()


async def get_example(call: CallbackQuery, state: FSMContext) -> None:
    info = await state.get_data()
    category = info.get('category')
    if category:
        match category:
            case 'Бот':
                example = 'бот.docx'
            case 'Сайт':
                example = 'сайт.docx'
            case 'Программа':
                example = 'бот.docx'
            case 'Дизайн':
                example = 'бот.docx'
            case _:
                await call.message.answer('Ошибка выбора, попробуйте вернуться в главное меню и начать заново')
                return
        await call.answer("Высылаю пример ТЗ...")
        doc = InputFile(f'bot/handlers/users/example/{example}', f'Пример_{category}.docx')
        await call.message.answer_document(doc)


async def get_document(message: Message, state: FSMContext) -> None:
    document_url = await message.document.get_url()
    await state.update_data(url=document_url)
    await message.answer("Пожелания по заказу?\nесли нету, нажмите на кнопку Пропустить", reply_markup=wishes_keyboard)
    await StatesOrder.WISHES.set()


async def get_wishes(message: Message, state: FSMContext) -> None:
    if not len(message.text) <= 300:
        raise ErrorWishes
    await state.update_data(wishes=message.text)
    await message.answer('Укажите желаемые сроки исполнения заказа')
    await StatesOrder.DATATIME.set()


async def skip_wishes(message: Message, state: FSMContext) -> None:
    await state.update_data(wishes='')
    await message.answer('Укажите желаемые сроки исполнения заказа')
    await StatesOrder.DATATIME.set()


async def get_datatime(message: Message, state: FSMContext) -> None:
    await state.update_data(datatime=message.text)
    await message.answer("Предложите цену за проект(В рублях)")
    await StatesOrder.PRICE.set()


async def get_price(message: Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        raise ErrorPrice
    await state.update_data(price=message.text)
    await message.answer('Введите способ связи (ссылку на соц.сеть, никнейм телеграмм и т.д)')
    await StatesOrder.LINK.set()


async def get_link(message: Message, state: FSMContext) -> None:
    await state.update_data(link=message.text)
    await message.answer("Ваша заявка создана и будет рассмотрена в ближайшее время", reply_markup=main_keyboard)
    await send_order_to_chat(message, state)
    await state.finish()


async def send_order_to_chat(message: Message, state: FSMContext) -> None:
    info = await state.get_data()
    order_id = await create_orders(info)
    order_admin_button = [
        InlineKeyboardButton("Принять", callback_data=f'{message.from_id}_1_{order_id}'),
        InlineKeyboardButton("Отклонить", callback_data=f'{message.from_id}_0_{order_id}')
    ]
    order_admin_keyboard = InlineKeyboardMarkup().add(*order_admin_button)
    document_bytes = InputFile(BytesIO(await get_bytes_document(info['url'])), filename=f'{message.from_id}.docx')
    msg = f'Категория:{info["category"]}\nСроки:{info["datatime"]}\nЦена:{info["price"]}\nПожелания:{info["wishes"]}\nСпособ связи:{info["link"]}'
    await message.bot.send_document(group_id, document_bytes, caption=msg, reply_markup=order_admin_keyboard)
    workers = await Worker.all()
    workers_not = [f'{work.username}' for work in workers if info['category'].lower() in str(work.category).lower()]
    await message.bot.send_message(group_id, 'Заказ вашей категории\n' + '\n'.join(workers_not))


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(get_scope_choice, text=scope_button, state='*', is_user=True)
    dp.register_callback_query_handler(get_example, text='example', state=StatesOrder.WAIT, is_user=True)
    dp.register_message_handler(get_document, content_types='document', state=StatesOrder.WAIT, is_user=True)
    dp.register_message_handler(skip_wishes, text=wishes_button[0], state=StatesOrder.WISHES, is_user=True)
    dp.register_message_handler(get_wishes, state=StatesOrder.WISHES, is_user=True)
    dp.register_message_handler(get_datatime, state=StatesOrder.DATATIME, is_user=True)
    dp.register_message_handler(get_price, state=StatesOrder.PRICE, is_user=True)
    dp.register_message_handler(get_link, state=StatesOrder.LINK, is_user=True)
