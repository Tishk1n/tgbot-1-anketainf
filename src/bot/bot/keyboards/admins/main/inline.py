from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_show_buttons = [
    InlineKeyboardButton('Отправить на исправление', callback_data='send'),
    InlineKeyboardButton('Удалить', callback_data='delete'),
    InlineKeyboardButton('Вернуться', callback_data='back_to'),
]
admin_show_keyboard = InlineKeyboardMarkup(row_width=2).add(*admin_show_buttons)
