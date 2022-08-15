from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ParseMode

from bot.database.models import User, Admin
from bot.database.models.deleted import Deleted
from bot.keyboards.admins.main.inline import admin_show_keyboard
from bot.keyboards.admins.main.reply import admin_main_keyboard, admin_main_buttons


async def cmd_admin(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('welcome to admin panel', reply_markup=admin_main_keyboard)


async def show_user(message: Message, state: FSMContext) -> None:
    await state.finish()
    users = await User.all()
    if users:
        users_ids = [user.id_tg for user in users]
        keyboard = InlineKeyboardMarkup(row_width=2)
        info = await state.get_data()
        now = info['now'] if info.get('now') else 0
        end = now + 8
        end = end if end < len(users_ids) else len(users_ids)
        buttons = [InlineKeyboardButton(users_ids[i], callback_data=users_ids[i]) for i in range(now, end)]
        end_buttons = [InlineKeyboardButton('<', callback_data='back'), InlineKeyboardButton('>', callback_data='next')]
        keyboard.row(*buttons)
        keyboard.add(*end_buttons)
        await message.answer('Список анкет', reply_markup=keyboard)
        return
    await message.answer('Пустой список')


async def btn_back(call: CallbackQuery, state: FSMContext) -> None:
    info = await state.get_data()
    now = info['now'] if info.get('now') else 0
    now = now - 8 if now >= 8 else 0
    await state.update_data(now=now)
    call.message.from_user = call.from_user
    await call.message.delete()
    await show_user(call.message, state)


async def btn_next(call: CallbackQuery, state: FSMContext) -> None:
    users_len = await User.all().count()
    info = await state.get_data()
    now = info['now'] if info.get('now') else 0
    now = now + 8 if now + 8 <= users_len - 1 else users_len - 1
    await state.update_data(now=now)
    call.message.from_user = call.from_user
    await call.message.delete()
    await show_user(call.message, state)


async def show_quest(call: CallbackQuery, state: FSMContext) -> None:
    user = await User.get(id_tg=int(call.data))
    await state.update_data(id_tg=call.data)
    await call.message.edit_text(user.to_str(), reply_markup=admin_show_keyboard, parse_mode=ParseMode.HTML)


async def send_to_fix(call: CallbackQuery, state: FSMContext) -> None:
    info = await state.get_data()
    user_id = int(info['id_tg']) if info.get('id_tg') else None
    user = await User.get(id_tg=user_id)
    await user.delete()
    await call.bot.send_message(user_id, 'Ваша анкета была отклонена, необходимо заполнить заявку еще раз')
    call.message.from_user = call.from_user
    await show_user(call.message, state)


async def delete_user(call: CallbackQuery, state: FSMContext) -> None:
    info = await state.get_data()
    user_id = int(info['id_tg']) if info.get('id_tg') else None
    user = await User.get(id_tg=user_id)
    await user.delete()
    await Deleted(id_tg=user_id).save()
    await call.bot.send_message(user_id, 'Ваша анкета была отклонена без возможности исправления')
    call.message.from_user = call.from_user
    await show_user(call.message, state)


async def back_to(call: CallbackQuery, state: FSMContext) -> None:
    call.message.from_user = call.from_user
    await call.message.delete()
    await show_user(call.message, state)


async def help(message: Message, state: FSMContext) -> None:
    await message.answer(
        'Добавить админа:/new_admin <user_id>'
    )


async def add_admin(message: Message, state: FSMContext) -> None:
    user_id = message.text.split()[1]
    await Admin(id_tg=int(user_id)).save()
    await message.answer(f'Пользователь {user_id} теперь админ')


def register(dp: Dispatcher):
    dp.register_message_handler(cmd_admin, commands='admin', state='*', is_admin=True)
    dp.register_message_handler(show_user, text=admin_main_buttons[0], is_admin=True)
    dp.register_callback_query_handler(btn_back, text='back', is_admin=True)
    dp.register_callback_query_handler(btn_next, text='next', is_admin=True)
    dp.register_callback_query_handler(send_to_fix, text='send', is_admin=True)
    dp.register_callback_query_handler(delete_user, text='delete', is_admin=True)
    dp.register_callback_query_handler(back_to, text='back_to', is_admin=True)
    dp.register_callback_query_handler(show_quest, is_admin=True)
    dp.register_message_handler(help, commands='help', state='*', is_admin=True)
    dp.register_message_handler(help, text=admin_main_buttons[1], state='*', is_admin=True)
    dp.register_message_handler(add_admin, commands='new_admin', state='*', is_admin=True)
