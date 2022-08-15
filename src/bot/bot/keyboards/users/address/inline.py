from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

address_buttons = [
    InlineKeyboardButton("Собственность", callback_data='cob'),
    InlineKeyboardButton("Социальный найм", callback_data='coz'),
    InlineKeyboardButton("Аренда", callback_data='are'),
    InlineKeyboardButton("Воинская часть", callback_data='voi'),
    InlineKeyboardButton("Жильё родственников", callback_data='jr'),
    InlineKeyboardButton("Коммунальная квартира", callback_data='com')
]
address_keyboard = InlineKeyboardMarkup(row_width=1).add(*address_buttons)
