from aiogram.dispatcher.filters.state import StatesGroup, State


class NewWorker(StatesGroup):
    USERNAME = State()
    CATEGORY = State()
    STACK = State()
