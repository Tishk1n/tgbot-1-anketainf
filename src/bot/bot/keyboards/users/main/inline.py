from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

begin_get_quests_button = InlineKeyboardButton('Перейти к вопросам', callback_data='begin_quest')
begin_get_quests_keyboard = InlineKeyboardMarkup().add(begin_get_quests_button)


continue_menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Закончил", callback_data='end'),
)