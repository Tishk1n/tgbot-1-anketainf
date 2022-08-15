from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

income_buttons = [
    InlineKeyboardButton("2-НДФЛ", callback_data='ndfl'),
    InlineKeyboardButton("Выписка из ПФР", callback_data='pfr'),
    InlineKeyboardButton("Налоговая декларация", callback_data='nd'),
    InlineKeyboardButton("Справка о размере пенсии", callback_data='srp'),
    InlineKeyboardButton("Справка по форме банка", callback_data='spfb'),
    InlineKeyboardButton("Выписка из похозяйственной книги", callback_data='vph'),
    InlineKeyboardButton("Без подтверждения", callback_data='notpay')
]

income_keyboard = InlineKeyboardMarkup(row_width=1).add(*income_buttons)