from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from bot.database.models.worker import Worker
from bot.keyboards.admins.main.reply import admin_main_keyboard, admin_main_button
from bot.states.admins.new_worker import NewWorker


async def main_admin(message: Message, state: FSMContext) -> None:
    await message.answer('Welcome to admin panel', reply_markup=admin_main_keyboard)


async def show_all_worker(message: Message, state: FSMContext) -> None:
    workers = await Worker.all()
    if not workers:
        await message.answer('Пустой список')
        return
    workers = [work.to_str() for work in workers]
    workers_str = "\n\n".join(workers)
    await message.answer(f'Список разработчиков:\n {workers_str}', parse_mode=ParseMode.HTML)


async def add_new_admin(message: Message, state: FSMContext) -> None:
    await message.answer(f'@{message.from_user.username}, введите юзернейм разработчика')
    await NewWorker.USERNAME.set()


async def get_username(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await message.answer(f'@{message.from_user.username}, введите категорию разработки')
    await NewWorker.CATEGORY.set()


async def get_category(message: Message, state: FSMContext) -> None:
    await state.update_data(category=message.text)
    await message.answer(f'@{message.from_user.username}, введите стек разработчика')
    await NewWorker.STACK.set()


async def get_stack(message: Message, state: FSMContext) -> None:
    info = await state.get_data()
    worker = Worker(username=info["username"], category=info["category"], stack=message.text)
    await worker.save()
    await message.answer(worker.to_str(), parse_mode=ParseMode.HTML)
    await state.finish()


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(main_admin, commands='admins', state='*', is_admin=True)
    dp.register_message_handler(show_all_worker, text=admin_main_button[0], is_admin=True)
    dp.register_message_handler(add_new_admin, text=admin_main_button[1], is_full_admin=True)
    dp.register_message_handler(get_username, state=NewWorker.USERNAME, is_full_admin=True)
    dp.register_message_handler(get_category, state=NewWorker.CATEGORY, is_full_admin=True)
    dp.register_message_handler(get_stack, state=NewWorker.STACK, is_full_admin=True)
