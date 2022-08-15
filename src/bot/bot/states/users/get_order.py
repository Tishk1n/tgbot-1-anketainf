from aiogram.dispatcher.filters.state import StatesGroup, State


class StatesOrder(StatesGroup):
    WAIT = State()
    WISHES = State()
    DATATIME = State()
    PRICE = State()
    LINK = State()
