from aiogram.dispatcher.filters.state import StatesGroup, State


class Change(StatesGroup):
    change = State()

    PASSPORT = State()
    INCOME = State()
    FACT_ADDRESS = State()
    TIME_LIVE_THIS = State()
    ADDRESS = State()
    STUDY = State()
    MATERIAL_STATUS = State()

    MARRIAGE = State()
    SOCIAL = State()

    EMAIL = State()
    PHONE = State()
    SNILS = State()

    BUSYNESS_TYPE = State()

    CARD_TYPE = State()
    CARD_UPLOAD = State()
    CARD_MYSELF = State()

    BEGIN_WORK = State()
    FULL_NAME_COMPANY = State()
    ADDRESS_COMPANY = State()

    SITE_COMPANY = State()
    PHONE_COMPANY = State()
    FIRST_WORK = State()
    POST = State()

    MAIN_INCOME = State()
    BACK_INCOME = State()
    CREDIT = State()
    CREDIT_CARD = State()

    LIMIT = State()

    CAR = State()
    PROPERTY = State()
