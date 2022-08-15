from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

busyness_button = [
    InlineKeyboardButton("Коммерческая", callback_data='kom'),
    InlineKeyboardButton("Бюджетная", callback_data='byd'),
    InlineKeyboardButton("Свой бизнес", callback_data='cdoy_buz'),
    InlineKeyboardButton("По найму", callback_data='naym'),
    InlineKeyboardButton("Пенсионер", callback_data='pencioner'),
    InlineKeyboardButton("ИП", callback_data='ip'),
]
busyness_keyboard = InlineKeyboardMarkup(row_width=1).add(*busyness_button)

card_buttons = [
    InlineKeyboardButton('Загрузить', callback_data='upload'),
    InlineKeyboardButton('Ввести в ручную', callback_data='myself')
]
card_keyboard = InlineKeyboardMarkup(row_width=1).add(*card_buttons)
