from aiogram.types import ReplyKeyboardMarkup


wishes_button = ["Пропустить"]
wishes_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(*wishes_button)
