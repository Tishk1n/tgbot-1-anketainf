import asyncio
import os
from datetime import datetime
last_time = datetime.now()
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor, exceptions
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from sqlite_db import Database
from aiogram.dispatcher.filters.state import StatesGroup, State
import config
import logging
import markups as mp



logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('db.db')


markdown = """
*bold text*
_italic text_
[text](URL)
"""

async def startup(_):
    print('Бот подключен')

class anketa(StatesGroup):
    photo_pasport = State()
    photo_answer = State()
    prome = State()
    vubor_prome = State()
    adres = State()
    time = State()
    osnovanie = State()
    education = State()
    family = State()
    brak = State()
    cosual = State()
    e_mail = State()
    phone_number = State()
    cnulc = State()
    zanya = State()
    card = State()
    start_work = State()
    start_work2 = State()
    dolg = State()
    dohod = State()
    dohod2 = State()
    credit = State()
    credit_card = State()
    limit = State()
    car = State()
    cob = State()

startbutton = KeyboardButton('Заполнить Анкету ✓')
startkb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(startbutton)

adminkb = types.ReplyKeyboardMarkup(resize_keyboard=True)
butt1 = types.KeyboardButton(text = "Посмотреть анкеты")
butt2 = types.KeyboardButton(text = "Добавить администратора")
butt3 = types.KeyboardButton(text = "Открытая линия")

adminkb.add(butt1).add(butt2)
adminkb.add(butt3)



test = InlineKeyboardButton("Принять", callback_data='prinyal')
test2 = InlineKeyboardButton("Отклонить", callback_data='otklonil')
test1 = InlineKeyboardMarkup().row(mp.inline_btn_fin2, test, test2)


@dp.message_handler(text=['/admin'])
async def admin(message: types.Message):
    await message.answer("Ваша админ панель:", reply_markup=adminkb)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup=startkb)

@dp.message_handler(text=['Заполнить Анкету ✓'])
async def start1(message: types.Message):
    if not db.examination(message.from_user.id):
        db.add(message.from_user.id)
    if not db.examination_com(message.from_user.id):
        db.add_com(message.from_user.id)
    await message.answer('Привет! Я помощник Лилии, задам тебе несколько вопросов, чтобы заполнить твою анкету клиента.\n'
                         'Пожалуйста, отвечай на все  вопросы в одном сообщении, потому что после каждого твоего ответа автоматически задается следующий вопрос', reply_markup=mp.start)

@dp.callback_query_handler(text=['start'])
async def anketa_start(call: types.CallbackQuery):
    user_anketa = db.user_anketa(call.from_user.id)
    if user_anketa == 0:
        db.add_anketa(call.from_user.id, user_anketa + 1)
        await bot.send_message(call.from_user.id, 'Сейчас заполняем раздел Личная информация')
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, 'Загрузите фотографии всех страниц паспорта\n'
                                              'P.S: Когда загрузите все фото - нажмите кнопку "ЗАКОНЧИЛ"', reply_markup=mp.continue_menu)
        await anketa.photo_pasport.set()
    elif user_anketa == 1:
        await bot.send_message(call.from_user.id, 'Ты уже заполнил свою анкету')

@dp.callback_query_handler(text=['start1'])
async def anketa_start1(call: types.CallbackQuery):
    user_anketa = db.user_anketa(call.from_user.id)
    if user_anketa == 0:
        db.add_anketa(call.from_user.id, user_anketa + 1)
        await bot.send_message(call.from_user.id, 'Сейчас заполняем раздел Личная информация')
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, 'Загрузите фотографии всех страниц паспорта\n'
                                              'P.S: Когда загрузите все фото - нажмите кнопку "ЗАКОНЧИЛ"', reply_markup=mp.continue_menu)
        await anketa.photo_pasport.set()
    elif user_anketa == 1:
        await bot.send_message(call.from_user.id, 'Ты уже заполнил свою анкету')


@dp.message_handler(content_types=['photo'], state=anketa.photo_pasport)
async def photo(message: types.Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    user_id = str(message.from_user.id)
    await bot.download_file(file_path, f"images{user_id}/" + file_id)
    await anketa.photo_pasport.set()




@dp.callback_query_handler(text=['stop'], state=anketa.photo_pasport)
async def photo(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id,'Выберите способ подтверждения дохода', reply_markup=mp.pay_d)
    await anketa.vubor_prome.set()

@dp.callback_query_handler(text=['ndfl'], state=anketa.vubor_prome)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "2-НДФЛ"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свой адрес фактического проживания:')
    await anketa.adres.set()

@dp.callback_query_handler(text=['pfr'], state=anketa.vubor_prome)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Выписка из ПФР"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свой адрес фактического проживания:')
    await anketa.adres.set()

@dp.callback_query_handler(text=['nd'], state=anketa.vubor_prome)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Налоговая декларация"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свой адрес фактического проживания:')
    await anketa.adres.set()

@dp.callback_query_handler(text=['srp'], state=anketa.vubor_prome)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Справка о размере пенсии"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свой адрес фактического проживания:')
    await anketa.adres.set()

@dp.callback_query_handler(text=['spfb'], state=anketa.vubor_prome)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Справка по форме банка"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свой адрес фактического проживания:')
    await anketa.adres.set()

@dp.callback_query_handler(text=['vph'], state=anketa.vubor_prome)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Выписка из похозяйственной книги"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свой адрес фактического проживания:')
    await anketa.adres.set()

@dp.callback_query_handler(text=['notpay'], state=anketa.vubor_prome)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Без подтверждения"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свой адрес фактического проживания:')
    await anketa.adres.set()

@dp.message_handler(state=anketa.adres)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_adres(message.from_user.id, text)
    await bot.send_message(message.from_user.id, 'Сколько времени вы проживаете по этому адресу? ')
    await anketa.time.set()

@dp.message_handler(state=anketa.time)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_time_live(message.from_user.id, text)
    await bot.send_message(message.from_user.id, 'Выберите основание проживания', reply_markup=mp.osnv)
    await anketa.osnovanie.set()

@dp.callback_query_handler(text=['cob'], state=anketa.osnovanie)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Собственность"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите своё образование', reply_markup=mp.educ)
    await anketa.education.set()

@dp.callback_query_handler(text=['coz'], state=anketa.osnovanie)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Социальный найм"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите своё образование', reply_markup=mp.educ)
    await anketa.education.set()

@dp.callback_query_handler(text=['are'], state=anketa.osnovanie)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Аренда"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите своё образование', reply_markup=mp.educ)
    await anketa.education.set()

@dp.callback_query_handler(text=['voi'], state=anketa.osnovanie)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Воинская часть"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите своё образование', reply_markup=mp.educ)
    await anketa.education.set()

@dp.callback_query_handler(text=['jr'], state=anketa.osnovanie)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Жильё родственников"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите своё образование', reply_markup=mp.educ)
    await anketa.education.set()

@dp.callback_query_handler(text=['com'], state=anketa.osnovanie)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Коммунальная квартира"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите своё образование', reply_markup=mp.educ)
    await anketa.education.set()

@dp.callback_query_handler(text=['uc'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Ученая степень"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['2v'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Два высших и более"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['vuc'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Высшее"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['nv'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Неоконченное высшее"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['cz'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Среднее специальное"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['cr'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Среднее"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['nuvc'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Ниже среднего"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['rm'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Российское МВА"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()

@dp.callback_query_handler(text=['umba'], state=anketa.education)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Иностранное МВА"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите семейное положение:', reply_markup=mp.fam)
    await anketa.family.set()




@dp.callback_query_handler(text=['jz'], state=anketa.family)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Женат/замужем"
    db.add_family(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Брачный контракт', reply_markup=mp.bra)
    await anketa.brak.set()

@dp.callback_query_handler(text=['gr'], state=anketa.family)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Гражданский брак"
    db.add_family(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Брачный контракт', reply_markup=mp.bra)
    await anketa.brak.set()

@dp.callback_query_handler(text=['hz'], state=anketa.family)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Холост/не замужем"
    db.add_family(call.from_user.id, vybor)
    db.add_brak(call.from_user.id, "Супруга/и нет")
    db.add_cosual(call.from_user.id, "Супруга/и нет")
    await bot.send_message(call.from_user.id, 'Укажите свою электронную почту')
    await anketa.e_mail.set()


@dp.callback_query_handler(text=['raz'], state=anketa.family)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Разведен(-а)"
    db.add_family(call.from_user.id, vybor)
    db.add_brak(call.from_user.id, "Супруга/и нет")
    db.add_cosual(call.from_user.id, "Супруга/и нет")
    await bot.send_message(call.from_user.id, 'Укажите свою электронную почту')
    await anketa.e_mail.set()

@dp.callback_query_handler(text=['vdo'], state=anketa.family)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Вдовец/вдова"
    db.add_family(call.from_user.id, vybor)
    db.add_brak(call.from_user.id, "Супруга/и нет")
    db.add_cosual(call.from_user.id, "Супруга/и нет")
    await bot.send_message(call.from_user.id, 'Укажите свою электронную почту')
    await anketa.e_mail.set()


@dp.callback_query_handler(text=['yes'], state=anketa.brak)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Есть"
    db.add_brak(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите соц. статус супруга(-и)', reply_markup=mp.cosual_c)
    await anketa.cosual.set()

@dp.callback_query_handler(text=['no'], state=anketa.brak)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Нет"
    db.add_brak(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите соц. статус супруга(-и)', reply_markup=mp.cosual_c)
    await anketa.cosual.set()

@dp.callback_query_handler(text=['bzc'], state=anketa.brak)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Будет заключен до сделки"
    db.add_brak(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Выберите соц. статус супруга(-и)')
    await anketa.cosual.set()


@dp.callback_query_handler(text=['work'], state=anketa.cosual)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Работает"
    db.add_cosual(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свою электронную почту')
    await anketa.e_mail.set()

@dp.callback_query_handler(text=['nowork'], state=anketa.cosual)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Не работает"
    db.add_cosual(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свою электронную почту')
    await anketa.e_mail.set()

@dp.callback_query_handler(text=['pen'], state=anketa.cosual)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "На пенсии"
    db.add_cosual(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Укажите свою электронную почту')
    await anketa.e_mail.set()



@dp.message_handler(state=anketa.e_mail)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_e_mail(message.from_user.id, text)
    await bot.send_message(message.from_user.id, 'Укажите свой номер телефона')
    await anketa.phone_number.set()



@dp.message_handler(state=anketa.phone_number)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_phone_number(message.from_user.id, text)
    await bot.send_message(message.from_user.id, 'Напишите номер своего СНИЛС')
    await anketa.cnulc.set()

@dp.message_handler(state=anketa.cnulc)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_cnulc(message.from_user.id, text)
    await asyncio.sleep(3)
    await bot.send_message(message.from_user.id, 'Сейчас заполняем раздел Занятость')
    await asyncio.sleep(1)
    await bot.send_message(message.from_user.id, 'Выберите тип занятости', reply_markup=mp.zan)
    await anketa.zanya.set()

@dp.callback_query_handler(text=['kom'], state=anketa.zanya)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Коммерческая"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Загрузить  карточку компании или ввести данные вручную?', reply_markup=mp.card_m)
    await anketa.card.set()

@dp.callback_query_handler(text=['byd'], state=anketa.zanya)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Бюджетная"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Загрузить  карточку компании или ввести данные вручную?', reply_markup=mp.card_m)
    await anketa.card.set()

@dp.callback_query_handler(text=['cdoy_buz'], state=anketa.zanya)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Свой бизнес"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Загрузить  карточку компании или ввести данные вручную?', reply_markup=mp.card_m)
    await anketa.card.set()

@dp.callback_query_handler(text=['naym'], state=anketa.zanya)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "По найму"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Загрузить  карточку компании или ввести данные вручную?', reply_markup=mp.card_m)
    await anketa.card.set()

@dp.callback_query_handler(text=['pencioner'], state=anketa.zanya)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Пенсионер"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Загрузить  карточку компании или ввести данные вручную?', reply_markup=mp.card_m)
    await anketa.card.set()

@dp.callback_query_handler(text=['ip'], state=anketa.zanya)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "ИП"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(call.from_user.id, 'Загрузить  карточку компании или ввести данные вручную?', reply_markup=mp.card_m)
    await anketa.card.set()

@dp.callback_query_handler(text=['down'], state=anketa.card)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, 'Отправьте карточку компании')
    await anketa.card.set()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=anketa.card)
async def sd(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    path = rf"C:\Users\ildar\PycharmProjects\IP_PL\card{user_id}"
    db.add_card(message.from_user.id, "document")
    await message.document.download(path)
    await message.answer('Напишите дату начала работы в указанной организации')
    await anketa.start_work.set()

@dp.message_handler(content_types=['photo'], state=anketa.card)
async def photo(message: types.Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    user_id = str(message.from_user.id)
    db.add_card(message.from_user.id, "document")
    await bot.download_file(file_path, f"card{user_id}/" + file_id)
    await message.answer('Напишите дату начала работы в указанной организации')
    await anketa.start_work.set()

@dp.message_handler(content_types=['text'], state=anketa.card)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    user_id = str(message.from_user.id)
    db.add_card(message.from_user.id, text)
    await message.answer('Напишите дату начала работы в указанной организации')
    await anketa.start_work.set()


class card_work(StatesGroup):
    name = State()
    adres_com = State()
    years = State()
    sait = State()
    number_com = State()
    count = State()
    cfera = State()


@dp.callback_query_handler(text=['vvesti'], state=anketa.card)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    db.add_card(call.from_user.id, 'vvesti')
    await bot.send_message(call.from_user.id, 'Укажите полное наименование компании')
    await card_work.name.set()

@dp.message_handler(state=card_work.name)
async def sd(message: types.Message, state: FSMContext):
    text = message.text
    db.add_name(message.from_user.id, text)
    await message.answer('Укажите фактический адрес компании')
    await card_work.adres_com.set()

@dp.message_handler(state=card_work.adres_com)
async def sd(message: types.Message, state: FSMContext):
    text = message.text
    db.add_adres_company(message.from_user.id, text)
    await message.answer('Сколько лет компания на рынке')
    await card_work.years.set()

@dp.message_handler(state=card_work.years)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_years(message.from_user.id, text)
    await message.answer('Укажите сайт компании')
    await card_work.sait.set()

@dp.message_handler(state=card_work.sait)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_saits(message.from_user.id, text)
    await message.answer('Напишите номер телефона компании')
    await card_work.number_com.set()

@dp.message_handler(state=card_work.number_com)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_number_com(message.from_user.id, text)
    await message.answer('Укажите численность персонала')
    await card_work.count.set()

@dp.message_handler(state=card_work.count)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_count(message.from_user.id, text)
    await message.answer('Укажите отраслевую сферу компании '
                         '(Транспорт/услуги/финансы/строительство/образование/медицина и т.д.)')
    await card_work.cfera.set()

@dp.message_handler(state=card_work.cfera)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_cfera(message.from_user.id, text)
    await message.answer('Напишите дату начала работы в указанной организации')
    await anketa.start_work.set()

@dp.message_handler(state=anketa.start_work)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_start_work(message.from_user.id, text)
    await message.answer('Напишите дату начала своей трудовой деятельности')
    await anketa.start_work2.set()

@dp.message_handler(state=anketa.start_work2)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_start_work2(message.from_user.id, text)
    await message.answer('Укажи название своей должности')
    await anketa.dolg.set()

@dp.message_handler(state=anketa.dolg)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_dolg(message.from_user.id, text)
    await asyncio.sleep(3)
    await message.answer('Сейчас заполняем раздел финансов')
    await asyncio.sleep(1)
    await message.answer('Укажите свой основной доход в месяц в рублях (Пример: 200000 руб.)')
    await anketa.dohod.set()

@dp.message_handler(state=anketa.dohod)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_dohod(message.from_user.id, text)
    await message.answer('Укажите свой дополнительный доход в месяц (если его нет, то напишите “нет”)')
    await anketa.dohod2.set()

@dp.message_handler(state=anketa.dohod2)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_dohod2(message.from_user.id, text)
    await message.answer('Если у вас есть кредиты, напишите сколько в месяц ты выплачиваешь на их погашение (Если кредитов нет, напиши “нет”, если их несколько проссумируй)')
    await anketa.credit.set()


@dp.message_handler(state=anketa.credit)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_credit(message.from_user.id, text)
    await message.answer('Если у вас есть кредитная карта, укажите сколько их у вас(1, 2, 3, 4)\n(Если карты  нет, напиши “нет”)')
    await anketa.credit_card.set()

@dp.message_handler(state=anketa.credit_card)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    text1 = text.lower()
    if text1 == "нет":
        db.add_credit_card(message.from_user.id, "нет")
        await message.answer('Сейчас заполняем раздел Активы')
        await asyncio.sleep(1)
        await message.answer('Если у вас в собственности есть автомобиль, укажите:\n'
                             '- Марка и модель\n'
                             '- стоимость\n'
                             '- год выпуска\n'
                             '- находится ли в залоге\n'
                             '(Если автомобиля нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
        await anketa.car.set()
    else:
        db.add_credit_card(message.from_user.id, text)
        await message.answer('Напишите, какой месячный лимит каждой карты через запятую (30 тыс., 50 тыс. и т.д.)')
        await anketa.limit.set()

@dp.message_handler(state=anketa.limit)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_limi(message.from_user.id, text)
    await asyncio.sleep(3)
    await message.answer('Сейчас заполняем раздел Активы')
    await asyncio.sleep(1)
    await message.answer('Если у вас в собственности есть автомобиль, укажите:\n'
                         '- Марка и модель\n'
                         '- стоимость\n'
                         '- год выпуска\n'
                         '- находится ли в залоге\n'
                         '(Если автомобиля нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
    await anketa.car.set()

@dp.message_handler(state=anketa.car)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_car(message.from_user.id, text)
    await message.answer('Если у вас в собственности есть недвижимость укажите:\n'
                         '- тип объекта (квартира, дом, участок …)\n'
                         '- находится ли в залоге\n'
                         '- право возникновения (Покупка, дарение, приватизация, наследство)\n'
                         '- площадь\n'
                         '- размер доли в %\n'
                         '- стоимость\n'
                         '- год приобретения\n'
                         '- адрес объекта\n'
                         '(Если объекта недвижимости нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
    await anketa.cob.set()

@dp.message_handler(state=anketa.cob)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_cob(message.from_user.id, text)
    await message.answer('Анкета готова', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['prinyal'])
async def fin(call: types.CallbackQuery):
    ud = call.from_user.id
    await bot.send_message(ud, "Ваша анкета принята")

@dp.callback_query_handler(text=['otklonil'])
async def fin(call: types.CallbackQuery):
    ud = call.from_user.id
    await bot.send_message(ud, "Ваша анкета отклонена, проверьте правильность заполнения")

@dp.callback_query_handler(text=['fin'])
async def fin(call: types.CallbackQuery):
    ud = call.from_user.id
    pay_d = db.user_pay_d(ud)
    adres = db.user_adres(ud)
    time_live = db.user_time_live(ud)
    osnovanie = db.user_osnovanie(ud)
    education = db.user_education(ud)
    family = db.user_family(ud)
    brak = db.user_brak(ud)
    cosual = db.user_cosual(ud)
    e_mail = db.user_e_mail(ud)
    phone_number = db.user_phone_number(ud)
    cnulc = db.user_cnulc(ud)
    zan = db.user_zan(ud)
    card = db.user_card(ud)
    name = db.user_name(ud)
    adres_company = db.user_adres_company(ud)
    years = db.user_years(ud)
    sait = db.user_sait(ud)
    number_com = db.user_number_com(ud)
    count = db.user_count(ud)
    cfera = db.user_cfera(ud)
    start_work = db.user_start_work(ud)
    start_work2 = db.user_start_work2(ud)
    dolg = db.user_dolg(ud)
    dohod = db.user_dohod(ud)
    dohod2 = db.user_dohod2(ud)
    credit = db.user_credit(ud)
    credit_card = db.user_credit_card(ud)
    limi = db.user_limi(ud)
    car = db.user_car(ud)
    cob = db.user_cob(ud)



    await bot.send_message(ud, 'Анкета пользователя: [{} {}](tg://user?id={})'.format(call.from_user.first_name, call.from_user.last_name, call.from_user.id), disable_web_page_preview=True, parse_mode="Markdown")
    files = os.listdir(f'images{ud}')
    for i in files:
        await bot.send_message(ud, 'Фото паспорта:')
        photo = open(f'images{ud}/{i}', 'rb')
        await bot.send_photo(ud, photo)
    await bot.send_message(ud, '___________________________\n')
    if card == "document":
        file = os.listdir(f'card{ud}')
        for i in file:
            photo = open(f'card{ud}/{i}', 'rb')
            await bot.send_message(ud, 'Карточка компании:')
            await bot.send_photo(ud, photo)
            await bot.send_message(ud, '___________________________\n')
            await bot.send_message(ud, f'1) Способ подтверждения дохода: {pay_d}\n'
                                       f'\n'
                                       f'2) Адрес фактического проживания: {adres}\n'
                                       f'\n'
                                       f'3) Проживаете по этому адресу: {time_live}\n'
                                       f'\n'
                                       f'4) Основание проживания: {osnovanie}\n'
                                       f'\n'
                                       f'5) Образование: {education}\n'
                                       f'\n'
                                       f'6) Семейное положение: {family}\n'
                                       f'\n'
                                       f'7) Брачный контракт: {brak}\n'
                                       f'\n'
                                       f'8) Социальный статус супруга(-и): {cosual}\n'
                                       f'\n'
                                       f'9) Электронная почта: {e_mail}\n'
                                       f'\n'
                                       f'10) Номер телефона: {phone_number}\n'
                                       f'\n'
                                       f'11) Номер СНИЛС: {cnulc}\n'
                                       f'\n'
                                       f'12) Тип занятости: {zan}\n'
                                       f'\n'
                                       f'13) Дата начала работы в указанной организации: {start_work}\n'
                                       f'\n'
                                       f'14) Дата начала своей трудовой деятельности: {start_work2}\n'
                                       f'\n'
                                       f'15) Название должности: {dolg}\n'
                                       f'\n'
                                       f'16) Основной доход в месяц в рублях: {dohod}\n'
                                       f'\n'
                                       f'17) Дополнительный доход в месяц: {dohod2}\n'
                                       f'\n'
                                       f'18) Сумма выплат на  погашение кредитов: {credit}\n'
                                       f'\n'
                                       f'19) Сколько кредитных карт: {credit_card}\n'
                                       f'\n'
                                       f'20) Месячный лимит каждой карты через запятую: {limi}'
                                       f'\n'
                                       f'21) Автомобиль\и: {car}\n'
                                       f'\n'
                                       f'22) Недвижимость\и: {cob}', reply_markup=mp.corective)
    if card == "vvesti":
        await bot.send_message(ud,"Карточка компании\n"
                                  "\n"
                                  f"1) Полное наименование компании: {name}\n"
                                  f"\n"
                                  f"2) Фактический адрес компании: {adres_company}\n"
                                  f"\n"
                                  f"3) Сколько лет компания на рынке: {years}\n"
                                  f"\n"
                                  f"4) Сайт компании: {sait}\n"
                                  f"\n"
                                  f"5) Номер телефона компании: {number_com}\n"
                                  f"\n"
                                  f"6) Численность персонала: {count}\n"
                                  f"\n"
                                  f"7) Отраслевая сфера компании: {cfera}\n"
                                  f"___________________________")
        await bot.send_message(ud, f'1) Способ подтверждения дохода: {pay_d}\n'
                                   f'\n'
                                   f'2) Адрес фактического проживания: {adres}\n'
                                   f'\n'
                                   f'3) Проживаете по этому адресу: {time_live}\n'
                                   f'\n'
                                   f'4) Основание проживания: {osnovanie}\n'
                                   f'\n'
                                   f'5) Образование: {education}\n'
                                   f'\n'
                                   f'6) Семейное положение: {family}\n'
                                   f'\n'
                                   f'7) Брачный контракт: {brak}\n'
                                   f'\n'
                                   f'8) Социальный статус супруга(-и): {cosual}\n'
                                   f'\n'
                                   f'9) Электронная почта: {e_mail}\n'
                                   f'\n'
                                   f'10) Номер телефона: {phone_number}\n'
                                   f'\n'
                                   f'11) Номер СНИЛС: {cnulc}\n'
                                   f'\n'
                                   f'12) Тип занятости: {zan}\n'
                                   f'\n'
                                   f'13) Дата начала работы в указанной организации: {start_work}\n'
                                   f'\n'
                                   f'14) Дата начала своей трудовой деятельности: {start_work2}\n'
                                   f'\n'
                                   f'15) Название должности: {dolg}\n'
                                   f'\n'
                                   f'16) Основной доход в месяц в рублях: {dohod}\n'
                                   f'\n'
                                   f'17) Дополнительный доход в месяц: {dohod2}\n'
                                   f'\n'
                                   f'18) Сумма выплат на  погашение кредитов: {credit}\n'
                                   f'\n'
                                   f'19) Сколько кредитных карт: {credit_card}\n'
                                   f'\n'
                                   f'20) Месячный лимит каждой карты через запятую: {limi}'
                                   f'\n'
                                   f'21) Автомобиль\и: {car}\n'
                                   f'\n'
                                   f'22) Недвижимость\и: {cob}', reply_markup=mp.corective_c)

        if card != "vvesti" and card != "document":
            await bot.send_message(ud, f"Карточка компании: {card}")
            await bot.send_message(ud, f'1) Способ подтверждения дохода: {pay_d}\n'
                                       f'\n'
                                       f'2) Адрес фактического проживания: {adres}\n'
                                       f'\n'
                                       f'3) Проживаете по этому адресу: {time_live}\n'
                                       f'\n'
                                       f'4) Основание проживания: {osnovanie}\n'
                                       f'\n'
                                       f'5) Образование: {education}\n'
                                       f'\n'
                                       f'6) Семейное положение: {family}\n'
                                       f'\n'
                                       f'7) Брачный контракт: {brak}\n'
                                       f'\n'
                                       f'8) Социальный статус супруга(-и): {cosual}\n'
                                       f'\n'
                                       f'9) Электронная почта: {e_mail}\n'
                                       f'\n'
                                       f'10) Номер телефона: {phone_number}\n'
                                       f'\n'
                                       f'11) Номер СНИЛС: {cnulc}\n'
                                       f'\n'
                                       f'12) Тип занятости: {zan}\n'
                                       f'\n'
                                       f'13) Дата начала работы в указанной организации: {start_work}\n'
                                       f'\n'
                                       f'14) Дата начала своей трудовой деятельности: {start_work2}\n'
                                       f'\n'
                                       f'15) Название должности: {dolg}\n'
                                       f'\n'
                                       f'16) Основной доход в месяц в рублях: {dohod}\n'
                                       f'\n'
                                       f'17) Дополнительный доход в месяц: {dohod2}\n'
                                       f'\n'
                                       f'18) Сумма выплат на  погашение кредитов: {credit}\n'
                                       f'\n'
                                       f'19) Сколько кредитных карт: {credit_card}\n'
                                       f'\n'
                                       f'20) Месячный лимит каждой карты через запятую: {limi}'
                                       f'\n'
                                       f'21) Автомобиль\и: {car}\n'
                                       f'\n'
                                       f'22) Недвижимость\и: {cob}', reply_markup=mp.corective_c)

        await bot.send_message(config.CHANNEL_ID, 'Анкета пользователя: [{} {}](tg://user?id={})'.format(call.from_user.first_name,
                                                                                          call.from_user.last_name,
                                                                                          call.from_user.id),
                               disable_web_page_preview=True, parse_mode="Markdown", reply_markup=test1)                       
                

        @dp.callback_query_handler(text=['fin2'])
        async def fin2(call: types.CallbackQuery):
            await bot.send_message(config.CHANNEL_ID, 'Анкета пользователя: [{} {}](tg://user?id={})'.format(call.from_user.first_name,
                                                                                            call.from_user.last_name,
                                                                                            call.from_user.id),
                                disable_web_page_preview=True, parse_mode="Markdown")


            files = os.listdir(f'images{ud}')
            for i in files:
                await bot.send_message(config.CHANNEL_ID, 'Фото паспорта:')
                photo = open(f'images{ud}/{i}', 'rb')
                await bot.send_photo(config.CHANNEL_ID, photo)
            await bot.send_message(config.CHANNEL_ID, '___________________________\n')
            if card == "document":
                file = os.listdir(f'card{ud}')
                for i in file:
                    photo = open(f'card{ud}/{i}', 'rb')
                    await bot.send_message(config.CHANNEL_ID, 'Карточка компании:')
                    await bot.send_photo(config.CHANNEL_ID, photo)
                    await bot.send_message(config.CHANNEL_ID, '___________________________\n')
                    await bot.send_message(config.CHANNEL_ID, f'1) Способ подтверждения дохода: {pay_d}\n'
                                        f'\n'
                                        f'2) Адрес фактического проживания: {adres}\n'
                                        f'\n'
                                        f'3) Проживаете по этому адресу: {time_live}\n'
                                        f'\n'
                                        f'4) Основание проживания: {osnovanie}\n'
                                        f'\n'
                                        f'5) Образование: {education}\n'
                                        f'\n'
                                        f'6) Семейное положение: {family}\n'
                                        f'\n'
                                        f'7) Брачный контракт: {brak}\n'
                                        f'\n'
                                        f'8) Социальный статус супруга(-и): {cosual}\n'
                                        f'\n'
                                        f'9) Электронная почта: {e_mail}\n'
                                        f'\n'
                                        f'10) Номер телефона: {phone_number}\n'
                                        f'\n'
                                        f'11) Номер СНИЛС: {cnulc}\n'
                                        f'\n'
                                        f'12) Тип занятости: {zan}\n'
                                        f'\n'
                                        f'13) Дата начала работы в указанной организации: {start_work}\n'
                                        f'\n'
                                        f'14) Дата начала своей трудовой деятельности: {start_work2}\n'
                                        f'\n'
                                        f'15) Название должности: {dolg}\n'
                                        f'\n'
                                        f'16) Основной доход в месяц в рублях: {dohod}\n'
                                        f'\n'
                                        f'17) Дополнительный доход в месяц: {dohod2}\n'
                                        f'\n'
                                        f'18) Сумма выплат на  погашение кредитов: {credit}\n'
                                        f'\n'
                                        f'19) Сколько кредитных карт: {credit_card}\n'
                                        f'\n'
                                        f'20) Месячный лимит каждой карты через запятую: {limi}\n'
                                        f'\n'
                                        f'21) Автомобиль\и: {car}\n'
                                        f'\n'
                                        f'22) Недвижимость\и: {cob}')
            if card == "vvesti":
                await bot.send_message(config.CHANNEL_ID, "Карточка компании\n"
                                        "\n"
                                        f"1) Полное наименование компании: {name}\n"
                                    f"\n"
                                    f"2) Фактический адрес компании: {adres_company}\n"
                                    f"\n"
                                    f"3) Сколько лет компания на рынке: {years}\n"
                                    f"\n"
                                    f"4) Сайт компании: {sait}\n"
                                    f"\n"
                                    f"5) Номер телефона компании: {number_com}\n"
                                    f"\n"
                                    f"6) Численность персонала: {count}\n"
                                    f"\n"
                                    f"7) Отраслевая сфера компании: {cfera}\n"
                                    f"___________________________")
            await bot.send_message(config.CHANNEL_ID, f'1) Способ подтверждения дохода: {pay_d}\n'
                                    f'\n'
                                    f'2) Адрес фактического проживания: {adres}\n'
                                    f'\n'
                                    f'3) Проживаете по этому адресу: {time_live}\n'
                                    f'\n'
                                    f'4) Основание проживания: {osnovanie}\n'
                                    f'\n'
                                    f'5) Образование: {education}\n'
                                    f'\n'
                                    f'6) Семейное положение: {family}\n'
                                    f'\n'
                                    f'7) Брачный контракт: {brak}\n'
                                    f'\n'
                                    f'8) Социальный статус супруга(-и): {cosual}\n'
                                    f'\n'
                                    f'9) Электронная почта: {e_mail}\n'
                                    f'\n'
                                    f'10) Номер телефона: {phone_number}\n'
                                    f'\n'
                                    f'11) Номер СНИЛС: {cnulc}\n'
                                    f'\n'
                                    f'12) Тип занятости: {zan}\n'
                                    f'\n'
                                    f'13) Дата начала работы в указанной организации: {start_work}\n'
                                    f'\n'
                                    f'14) Дата начала своей трудовой деятельности: {start_work2}\n'
                                    f'\n'
                                    f'15) Название должности: {dolg}\n'
                                    f'\n'
                                    f'16) Основной доход в месяц в рублях: {dohod}\n'
                                    f'\n'
                                    f'17) Дополнительный доход в месяц: {dohod2}\n'
                                    f'\n'
                                    f'18) Сумма выплат на  погашение кредитов: {credit}\n'
                                    f'\n'
                                    f'19) Сколько кредитных карт: {credit_card}\n'
                                    f'\n'
                                    f'20) Месячный лимит каждой карты через запятую: {limi}\n'
                                    f'\n'
                                    f'21) Автомобиль\и: {car}\n'
                                    f'\n'
                                    f'22) Недвижимость\и: {cob}')


            if card != "vvesti" and card != 'document':
                await bot.send_message(config.CHANNEL_ID, f"Карточка компании: {card}"
                                                        f"___________________________")
                await bot.send_message(config.CHANNEL_ID, f'1) Способ подтверждения дохода: {pay_d}\n'
                                        f'\n'
                                        f'2) Адрес фактического проживания: {adres}\n'
                                        f'\n'
                                        f'3) Проживаете по этому адресу: {time_live}\n'
                                        f'\n'
                                        f'4) Основание проживания: {osnovanie}\n'
                                        f'\n'
                                        f'5) Образование: {education}\n'
                                        f'\n'
                                        f'6) Семейное положение: {family}\n'
                                        f'\n'
                                        f'7) Брачный контракт: {brak}\n'
                                        f'\n'
                                        f'8) Социальный статус супруга(-и): {cosual}\n'
                                        f'\n'
                                        f'9) Электронная почта: {e_mail}\n'
                                        f'\n'
                                        f'10) Номер телефона: {phone_number}\n'
                                        f'\n'
                                        f'11) Номер СНИЛС: {cnulc}\n'
                                        f'\n'
                                        f'12) Тип занятости: {zan}\n'
                                        f'\n'
                                        f'13) Дата начала работы в указанной организации: {start_work}\n'
                                        f'\n'
                                        f'14) Дата начала своей трудовой деятельности: {start_work2}\n'
                                        f'\n'
                                        f'15) Название должности: {dolg}\n'
                                        f'\n'
                                        f'16) Основной доход в месяц в рублях: {dohod}\n'
                                        f'\n'
                                        f'17) Дополнительный доход в месяц: {dohod2}\n'
                                        f'\n'
                                        f'18) Сумма выплат на  погашение кредитов: {credit}\n'
                                        f'\n'
                                        f'19) Сколько кредитных карт: {credit_card}\n'
                                        f'\n'
                                        f'20) Месячный лимит каждой карты через запятую: {limi}\n'
                                        f'\n'
                                        f'21) Автомобиль\и: {car}\n'
                                        f'\n'
                                        f'22) Недвижимость\и: {cob}')



class corec(StatesGroup):
    corecziya = State()
    corecziya1 = State()
    cor1 = State()
    coradr = State()
    corjil = State()
    cor4 = State()
    cor5 = State()
    cor6 = State()
    cor7 = State()
    cor8 = State()
    cor9 = State()
    cor10 = State()
    cor11 = State()
    cor12 = State()
    cor13 = State()
    cor14 = State()
    cor15 = State()
    cor16 = State()
    cor17 = State()
    cor18 = State()
    cor19 = State()
    cor20 = State()
    cor21 = State()
    cor22 = State()


    cor_1 = State()
    cor_2 = State()
    cor_3 = State()
    cor_4 = State()
    cor_5 = State()
    cor_6 = State()
    cor_7 = State()


@dp.callback_query_handler(text=['cor_c'])
async def cor(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'Какой пункт хотите исправить? (число)')
    await corec.corecziya1.set()

@dp.message_handler(state=corec.corecziya1)
async def op(message: types.Message, state: FSMContext):
    t = int(message.text)
    if t == 1:
        await message.answer('Укажите полное наименование компании')
        await corec.cor_1.set()
    if t == 2:
        await message.answer('Укажите фактический адрес компании')
        await corec.cor_2.set()

    if t == 3:
        await message.answer('Сколько лет компания на рынке')
        await corec.cor_3.set()

    if t == 4:
        await message.answer('Укажите сайт компании')
        await corec.cor_4.set()

    if t == 5:
        await message.answer('Напишите номер телефона компании')
        await corec.cor_5.set()

    if t == 6:
        await message.answer('Укажите численность персонала')
        await corec.cor_6.set()

    if t == 7:
        await message.answer('Укажите отраслевую сферу компании\n'
                             '(Транспорт/услуги/финансы/строительство/образование/медицина и т.д.)')
        await corec.cor_7.set()

@dp.message_handler(state=corec.cor_1)
async def sd(message: types.Message, state: FSMContext):
    text = message.text
    db.add_name(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил карточку компании пункт 1 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor_2)
async def sd(message: types.Message, state: FSMContext):
    text = message.text
    db.add_adres_company(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил карточку компании пункт 2 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor_3)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_years(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил карточку компании пункт 3 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor_4)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_saits(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил карточку компании пункт 4 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor_5)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_number_com(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил карточку компании пункт 5 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor_6)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_count(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил карточку компании пункт 6 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor_7)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_cfera(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил карточку компании пункт 7 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()



@dp.callback_query_handler(text=['cor'])
async def cor(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'Какой пункт хотите исправить? (число)')
    await corec.corecziya.set()

@dp.message_handler(state=corec.corecziya)
async def op(message: types.Message, state: FSMContext):
    card = db.user_card(message.from_user.id)
    t = int(message.text)
    if t == 1:
        await message.answer('Выберите способ подтверждения дохода', reply_markup=mp.pray_d)
        await corec.cor1.set()
    if t == 2:
        await message.answer('Укажите свой адрес фактического проживания:')
        await corec.coradr.set()

    if t == 3:
        await message.answer('Сколько времени вы проживаете по этому адресу?')
        await corec.corjil.set()

    if t == 4:
        await message.answer('Выберите основание проживания', reply_markup=mp.osnva)
        await corec.cor4.set()

    if t == 5:
        await message.answer('Выберите своё образование', reply_markup=mp.educ_c)
        await corec.cor5.set()

    if t == 6:
        await message.answer('Выберите семейное положение:', reply_markup=mp.fam1)
        await corec.cor6.set()

    if t == 7:
        await message.answer('Брачный контракт', reply_markup=mp.bra1)
        await corec.cor7.set()

    if t == 8:
        await message.answer('Выберите соц. статус супруга(-и)', reply_markup=mp.cosual_c1)
        await corec.cor8.set()

    if t == 9:
        await message.answer('Укажите свою электронную почту')
        await corec.cor9.set()

    if t == 10:
        await message.answer('Укажите свой номер телефона')
        await corec.cor10.set()

    if t == 11:
        await message.answer('Напишите номер своего СНИЛС')
        await corec.cor11.set()

    if t == 12:
        await message.answer('Выберите тип занятости', reply_markup=mp.zan1)
        await corec.cor12.set()

    if t == 13:
        await message.answer('Напишите дату начала работы в указанной организации')
        await corec.cor13.set()

    if t == 14:
        await message.answer('Напишите дату начала своей трудовой деятельности')
        await corec.cor14.set()

    if t == 15:
        await message.answer('Укажи название своей должности')
        await corec.cor15.set()

    if t == 16:
        await message.answer('Укажите свой основной доход в месяц в рублях (Пример: 200000 руб.)')
        await corec.cor16.set()

    if t == 17:
        await message.answer('Укажите свой дополнительный доход в месяц (если его нет, то напишите “нет”)')
        await corec.cor17.set()

    if t == 18:
        await message.answer('Если у вас есть кредиты, напишите сколько в месяц ты выплачиваешь на их погашение (Если кредитов нет, напиши “нет”, если их несколько проссумируй)')
        await corec.cor18.set()

    if t == 19:
        await message.answer('Если у вас есть кредитная карта, укажите сколько их у вас(Если карты  нет, напиши “нет”)')
        await corec.cor19.set()

    if t == 20:
        await message.answer('Напишите, какой месячный лимит каждой карты через запятую (30 тыс., 50 тыс. и т.д.)')
        await corec.cor20.set()

    if t == 21:
        await message.answer('Если у вас в собственности есть автомобиль, укажите:\n'
                         '- Марка и модель\n'
                         '- стоимость\n'
                         '- год выпуска\n'
                         '- находится ли в залоге\n'
                         '(Если автомобиля нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
        await corec.cor21.set()

    if t == 22:
        await message.answer('Если у вас в собственности есть недвижимость укажите:\n'
                         '- тип объекта (квартира, дом, участок …)\n'
                         '- находится ли в залоге\n'
                         '- право возникновения (Покупка, дарение, приватизация, наследство)\n'
                         '- площадь\n'
                         '- размер доли в %\n'
                         '- стоимость\n'
                         '- год приобретения\n'
                         '- адрес объекта\n'
                         '(Если объекта недвижимости нет, напишите “нет”, если их 2 и больше, укажите информацию по каждому в ОДНОМ СООБЩЕНИИ)')
        await corec.cor22.set()






@dp.callback_query_handler(text=['ndfl1'], state=corec.cor1)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "2-НДФЛ"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 1 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['pfr1'], state=corec.cor1)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Выписка из ПФР"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 1 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['nd1'], state=corec.cor1)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Налоговая декларация"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 1 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['srp1'], state=corec.cor1)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Справка о размере пенсии"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 1 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['spfb1'], state=corec.cor1)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Справка по форме банка"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 1 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['vph1'], state=corec.cor1)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Выписка из похозяйственной книги"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={})анкету пункт 1 на {}'.format(call.from_user.first_name,call.from_user.last_name,call.from_user.id,vybor))
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['notpay1'], state=corec.cor1)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Без подтверждения"
    db.add_pay_d(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 1 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.message_handler(state=corec.coradr)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_adres(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 2 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(message.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()



@dp.message_handler(state=corec.corjil)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_time_live(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 3 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(message.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()



@dp.callback_query_handler(text=['cob1'], state=corec.cor4)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Собственность"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 4 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['coz1'], state=corec.cor4)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Социальный найм"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 4 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['are1'], state=corec.cor4)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Аренда"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 4 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['voi1'], state=corec.cor4)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Воинская часть"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 4 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['jr1'], state=corec.cor4)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Жильё родственников"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 4 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['com1'], state=corec.cor4)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Коммунальная квартира"
    db.add_osnovanie(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 4 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()




@dp.callback_query_handler(text=['uc1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Ученая степень"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['2v1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Два высших и более"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['vuc1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Высшее"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['nv1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Неоконченное высшее"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['cz1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Среднее специальное"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['cr1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Среднее"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['nuvc1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Ниже среднего"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['rm1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Российское МВА"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['umba1'], state=corec.cor5)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Иностранное МВА"
    db.add_education(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 5 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.callback_query_handler(text=['jz1'], state=corec.cor6)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Женат/замужем"
    db.add_family(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 6 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['gr1'], state=corec.cor6)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Гражданский брак"
    db.add_family(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 6 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['hz1'], state=corec.cor6)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Холост/не замужем"
    db.add_family(call.from_user.id, vybor)
    db.add_brak(call.from_user.id, "Супруга/и нет")
    db.add_cosual(call.from_user.id, "Супруга/и нет")
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 6 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.callback_query_handler(text=['raz1'], state=corec.cor6)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Разведен(-а)"
    db.add_family(call.from_user.id, vybor)
    db.add_brak(call.from_user.id, "Супруга/и нет")
    db.add_cosual(call.from_user.id, "Супруга/и нет")
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 6 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['vdo1'], state=corec.cor6)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Вдовец/вдова"
    db.add_family(call.from_user.id, vybor)
    db.add_brak(call.from_user.id, "Супруга/и нет")
    db.add_cosual(call.from_user.id, "Супруга/и нет")
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 6 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.callback_query_handler(text=['yes1'], state=corec.cor7)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Есть"
    db.add_brak(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 7 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['no1'], state=corec.cor7)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Нет"
    db.add_brak(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 7 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['bzc1'], state=corec.cor7)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Будет заключен до сделки"
    db.add_brak(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 7 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.callback_query_handler(text=['work1'], state=corec.cor8)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Работает"
    db.add_cosual(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 7 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['nowork1'], state=corec.cor8)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Не работает"
    db.add_cosual(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 8 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['pen1'], state=corec.cor8)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "На пенсии"
    db.add_cosual(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 8 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.message_handler(state=corec.cor9)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_e_mail(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 9 на {}'.format(message
        .from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(message.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.message_handler(state=corec.cor10)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_phone_number(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 10 на {}'.format(message
        .from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(message.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor11)
async def photo(message: types.Message, state: FSMContext):
    text = message.text
    db.add_cnulc(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 11 на {}'.format(message
        .from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(message.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.callback_query_handler(text=['kom1'], state=corec.cor12)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Коммерческая"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 12 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['byd1'], state=corec.cor12)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Бюджетная"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 12 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['cdoy_buz1'], state=corec.cor12)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Свой бизнес"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 12 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['naym1'], state=corec.cor12)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "По найму"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 12 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['pencioner1'], state=corec.cor12)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "Пенсионер"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 12 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.callback_query_handler(text=['ip1'], state=corec.cor12)
async def anketa_start(call: types.CallbackQuery, state: FSMContext):
    vybor = "ИП"
    db.add_zan(call.from_user.id, vybor)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 12 на {}'.format(
        call.from_user.first_name, call.from_user.last_name, call.from_user.id, vybor), disable_web_page_preview=True, parse_mode="Markdown")
    await bot.send_message(call.from_user.id, 'Анкета изменена', reply_markup=mp.fin)
    await state.finish()



@dp.message_handler(state=corec.cor13)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_start_work(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 13 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text), disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor14)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_start_work2(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 14 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor15)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_dolg(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 15 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.message_handler(state=corec.cor16)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_dohod(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 16 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor17)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_dohod2(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 17 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()



@dp.message_handler(state=corec.cor18)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_credit(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 18 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor19)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    if text.title() == "нет":
        db.add_credit_card(message.from_user.id, "нет")
        await bot.send_message(config.CHANNEL_ID,
                               'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 19 на {}'.format(
                                   message.from_user.first_name, message.from_user.last_name, message.from_user.id,
                                   text),
                               disable_web_page_preview=True, parse_mode="Markdown")
        await message.answer('Анкета изменена', reply_markup=mp.fin)
        await state.finish()
    else:
        db.add_credit_card(message.from_user.id, text)
        await bot.send_message(config.CHANNEL_ID,
                               'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 19 на {}'.format(
                                   message.from_user.first_name, message.from_user.last_name, message.from_user.id,
                                   text),
                               disable_web_page_preview=True, parse_mode="Markdown")
        await message.answer('Анкета изменена', reply_markup=mp.fin)
        await state.finish()

@dp.message_handler(state=corec.cor20)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_limi(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 20 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()

@dp.message_handler(state=corec.cor21)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_car(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 21 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()


@dp.message_handler(state=corec.cor22)
async def sd(message: types.Message, state: FSMContext):
    text = str(message.text)
    db.add_cob(message.from_user.id, text)
    await bot.send_message(config.CHANNEL_ID, 'Пользователь: [{} {}](tg://user?id={}) изменил анкету пункт 22 на {}'.format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, text),
                           disable_web_page_preview=True, parse_mode="Markdown")
    await message.answer('Анкета изменена', reply_markup=mp.fin)
    await state.finish()









if __name__=="__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=startup)