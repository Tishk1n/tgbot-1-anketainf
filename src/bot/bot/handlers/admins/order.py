from os import getenv

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from bot.database.models import Order


group_id = getenv('GROUP_ID')


async def action_order(call: CallbackQuery, state: FSMContext):
    user_id, action, order_id = call.data.split("_")
    info = await state.get_data()
    order = await Order.get(id=int(order_id))
    if not info:
        match action:
            case '0':
                mess = await call.message.answer('Напишите причину отказа (используйте reply на это сообщение)')
                await state.update_data(user_id=user_id, mess=mess.message_id)
                await order.delete()
            case '1':
                await call.bot.send_message(int(user_id), 'Ваша заявка рассмотрена и принята в работу')
                message = await call.message.reply(f'Заказ принял @{call.from_user.username}')
                await call.message.chat.pin_message(message.message_id)
                order.worker = f'@{call.from_user.username}'
                await order.save()
        await call.message.delete_reply_markup()
        return
    await call.message.answer('Опишите причину отказа для предыдущего заказа')
    await call.message.bot.send_message(group_id, '.', reply_to_message_id=info.get('mess'))


async def take_reason(message: Message, state: FSMContext):
    info = await state.get_data()
    if info:
        if info.get('mess') == message.reply_to_message.message_id:
            user_id = info['user_id']
            await message.bot.send_message(int(user_id), message.text)
            await message.answer('Ответ отправлен')
            await state.reset_data()
        else:
            await message.answer('Опишите причину отказа для предыдущего заказа')
            await message.bot.send_message(group_id, '.', reply_to_message_id=info.get('mess'))


def register(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(action_order, is_admin=True)
    dp.register_message_handler(take_reason, is_reply=True, is_admin=True)
