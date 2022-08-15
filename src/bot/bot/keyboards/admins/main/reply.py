from aiogram.types import ReplyKeyboardMarkup

admin_main_button = ["Список разработчиков", "Добавить", "Удалить"]
admin_main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*admin_main_button)
