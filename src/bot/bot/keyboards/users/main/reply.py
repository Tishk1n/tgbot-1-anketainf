from aiogram.types import ReplyKeyboardMarkup

main_button =["Сделать заказ"]
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*main_button)


scope_button = ["Бот", "Сайт", "Программа", "Дизайн", "Отмена"]
scope_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*scope_button)
