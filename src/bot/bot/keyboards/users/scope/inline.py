from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

example_button = [InlineKeyboardButton("Пример ТЗ", callback_data='example')]
example_keyboard = InlineKeyboardMarkup().add(*example_button)
