from aiogram.types import ReplyKeyboardMarkup

start_button = ['Заполнить Анкету ✓']
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*start_button)


cancel_button = ['Отмена']
cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*cancel_button)