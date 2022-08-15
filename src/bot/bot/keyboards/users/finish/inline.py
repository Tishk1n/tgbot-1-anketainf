from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

finish_buttons = [
    InlineKeyboardButton("Посмотреть анкету", callback_data='fin')
]
finish_keyboard = InlineKeyboardMarkup().add(*finish_buttons)


change_buttons = [
    InlineKeyboardButton("Исправить анкету", callback_data='change')
]
change_keyboard = InlineKeyboardMarkup().add(*change_buttons)
