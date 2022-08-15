from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

study_buttons = [
    InlineKeyboardButton("Ученая степень", callback_data='uc'),
    InlineKeyboardButton("Два высших и более", callback_data='2v'),
    InlineKeyboardButton("Высшее", callback_data='vuc'),
    InlineKeyboardButton("Неоконченное высшее", callback_data='nv'),
    InlineKeyboardButton("Среднее специальное", callback_data='cz'),
    InlineKeyboardButton("Среднее", callback_data='cr'),
    InlineKeyboardButton("Ниже среднего", callback_data='nuvc'),
    InlineKeyboardButton("Российское МВА", callback_data='rm'),
    InlineKeyboardButton("Иностранное МВА", callback_data='umba')
]

study_keyboards = InlineKeyboardMarkup(row_width=1).add(*study_buttons)
