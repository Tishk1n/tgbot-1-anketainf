from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

material_status_buttons = [
    InlineKeyboardButton("Женат/замужем", callback_data='jz'),
    InlineKeyboardButton("Гражданский брак", callback_data='gr'),
    InlineKeyboardButton("Холост/не замужем", callback_data='hz'),
    InlineKeyboardButton("Разведен(-а)", callback_data='raz'),
    InlineKeyboardButton("Вдовец/вдова", callback_data='vdo')
]
material_status_keyboard = InlineKeyboardMarkup(row_width=1).add(*material_status_buttons)


prenuptial_agreement_buttons = [
    InlineKeyboardButton("Есть", callback_data='yes'),
    InlineKeyboardButton("Нет", callback_data='no'),
    InlineKeyboardButton("Будет заключен до сделки", callback_data='bzc')
]
prenuptial_agreement_keyboard = InlineKeyboardMarkup(row_width=1).add(*prenuptial_agreement_buttons)


social_status_buttons = [
    InlineKeyboardButton("Работает", callback_data='work'),
    InlineKeyboardButton("Не работает", callback_data='nowork'),
    InlineKeyboardButton("На пенсии", callback_data='pen')
]
social_status_keyboard = InlineKeyboardMarkup(row_width=1).add(*social_status_buttons)

