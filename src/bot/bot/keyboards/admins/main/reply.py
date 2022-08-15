from aiogram.types import ReplyKeyboardMarkup

admin_main_buttons = ['Просмотр анкет', 'Помощь']
admin_main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*admin_main_buttons)


