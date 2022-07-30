from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup







inline_btn_start = InlineKeyboardButton('Перейти к вопросам', callback_data='start')
inline_btn_otmena = InlineKeyboardButton('Отмена', callback_data='start1')

inline_btn_ndfl = InlineKeyboardButton("2-НДФЛ", callback_data='ndfl')
inline_btn_pfr = InlineKeyboardButton("Выписка из ПФР", callback_data='pfr')
inline_btn_nd = InlineKeyboardButton("Налоговая декларация", callback_data='nd')
inline_btn_srp = InlineKeyboardButton("Справка о размере пенсии", callback_data='srp')
inline_btn_spfb = InlineKeyboardButton("Справка по форме банка", callback_data='spfb')
inline_btn_vph = InlineKeyboardButton("Выписка из похозяйственной книги", callback_data='vph')
inline_btn_notpay = InlineKeyboardButton("Без подтверждения", callback_data='notpay')


inline_btn_cob = InlineKeyboardButton("Собственность", callback_data='cob')
inline_btn_coz = InlineKeyboardButton("Социальный найм", callback_data='coz')
inline_btn_are = InlineKeyboardButton("Аренда", callback_data='are')
inline_btn_voi = InlineKeyboardButton("Воинская часть", callback_data='voi')
inline_btn_jr = InlineKeyboardButton("Жильё родственников", callback_data='jr')
inline_btn_com = InlineKeyboardButton("Коммунальная квартира", callback_data='com')

inline_btn_uc = InlineKeyboardButton("Ученая степень", callback_data='uc')
inline_btn_2v = InlineKeyboardButton("Два высших и более", callback_data='2v')
inline_btn_vuc = InlineKeyboardButton("Высшее", callback_data='vuc')
inline_btn_nv = InlineKeyboardButton("Неоконченное высшее", callback_data='nv')
inline_btn_cz = InlineKeyboardButton("Среднее специальное", callback_data='cz')
inline_btn_cr = InlineKeyboardButton("Среднее", callback_data='cr')
inline_btn_nuvc = InlineKeyboardButton("Ниже среднего", callback_data='nuvc')
inline_btn_rm = InlineKeyboardButton("Российское МВА", callback_data='rm')
inline_btn_umba = InlineKeyboardButton("Иностранное МВА", callback_data='umba')



inline_btn_jz = InlineKeyboardButton("Женат/замужем", callback_data='jz')
inline_btn_gr = InlineKeyboardButton("Гражданский брак", callback_data='gr')
inline_btn_hz = InlineKeyboardButton("Холост/не замужем", callback_data='hz')
inline_btn_raz = InlineKeyboardButton("Разведен(-а)", callback_data='raz')
inline_btn_vdo = InlineKeyboardButton("Вдовец/вдова", callback_data='vdo')


inline_btn_yes = InlineKeyboardButton("Есть", callback_data='yes')
inline_btn_no = InlineKeyboardButton("Нет", callback_data='no')
inline_btn_bzc = InlineKeyboardButton("Будет заключен до сделки", callback_data='bzc')


inline_btn_work = InlineKeyboardButton("Работает", callback_data='work')
inline_btn_nowork = InlineKeyboardButton("Не работает", callback_data='nowork')
inline_btn_pen = InlineKeyboardButton("На пенсии", callback_data='pen')


inline_btn_kom = InlineKeyboardButton("Коммерческая", callback_data='kom')
inline_btn_byd = InlineKeyboardButton("Бюджетная", callback_data='byd')
inline_btn_cvoy_buz = InlineKeyboardButton("Свой бизнес", callback_data='cdoy_buz')
inline_btn_naym = InlineKeyboardButton("По найму", callback_data='naym')
inline_btn_pencioner = InlineKeyboardButton("Пенсионер", callback_data='pencioner')
inline_btn_ip = InlineKeyboardButton("ИП", callback_data='ip')


inline_btn_down = InlineKeyboardButton("Загрузить карточку", callback_data='down')
inline_btn_vvesti = InlineKeyboardButton("Ввести вручную", callback_data='vvesti')


inline_btn_fin = InlineKeyboardButton("Посмотреть анкету", callback_data='fin')




ndfl = InlineKeyboardButton("2-НДФЛ", callback_data='ndfl1')
pfr = InlineKeyboardButton("Выписка из ПФР", callback_data='pfr1')
nd = InlineKeyboardButton("Налоговая декларация", callback_data='nd1')
srp = InlineKeyboardButton("Справка о размере пенсии", callback_data='srp1')
spfb = InlineKeyboardButton("Справка по форме банка", callback_data='spfb1')
vph = InlineKeyboardButton("Выписка из похозяйственной книги", callback_data='vph1')
notpay = InlineKeyboardButton("Без подтверждения", callback_data='notpay1')

pray_d = InlineKeyboardMarkup().row(ndfl)\
    .row(pfr)\
    .row(nd)\
    .row(srp)\
    .row(spfb)\
    .row(vph)\
    .row(notpay)\
    .row(inline_btn_otmena)\

cob = InlineKeyboardButton("Собственность", callback_data='cob1')
coz = InlineKeyboardButton("Социальный найм", callback_data='coz1')
are = InlineKeyboardButton("Аренда", callback_data='are1')
voi = InlineKeyboardButton("Воинская часть", callback_data='voi1')
jr = InlineKeyboardButton("Жильё родственников", callback_data='jr1')
com = InlineKeyboardButton("Коммунальная квартира", callback_data='com1')

osnva = InlineKeyboardMarkup().row(cob)\
    .row(coz)\
    .row(are)\
    .row(voi)\
    .row(jr)\
    .row(com)\
    .row(inline_btn_otmena)\




uc = InlineKeyboardButton("Ученая степень", callback_data='uc1')
_2v = InlineKeyboardButton("Два высших и более", callback_data='2v1')
vuc = InlineKeyboardButton("Высшее", callback_data='vuc1')
nv = InlineKeyboardButton("Неоконченное высшее", callback_data='nv1')
cz = InlineKeyboardButton("Среднее специальное", callback_data='cz1')
cr = InlineKeyboardButton("Среднее", callback_data='cr1')
nuvc = InlineKeyboardButton("Ниже среднего", callback_data='nuvc1')
rm = InlineKeyboardButton("Российское МВА", callback_data='rm1')
umba = InlineKeyboardButton("Иностранное МВА", callback_data='umba1')

educ_c = InlineKeyboardMarkup().row(uc)\
    .row(_2v)\
    .row(vuc)\
    .row(nv)\
    .row(cz)\
    .row(cr)\
    .row(nuvc)\
    .row(rm)\
    .row(umba)\
    .row(inline_btn_otmena)\


jz = InlineKeyboardButton("Женат/замужем", callback_data='jz1')
gr = InlineKeyboardButton("Гражданский брак", callback_data='gr1')
hz = InlineKeyboardButton("Холост/не замужем", callback_data='hz1')
raz = InlineKeyboardButton("Разведен(-а)", callback_data='raz1')
vdo = InlineKeyboardButton("Вдовец/вдова", callback_data='vdo1')

fam1 = InlineKeyboardMarkup().row(jz)\
    .row(gr)\
    .row(hz)\
    .row(raz)\
    .row(vdo)\
    .row(inline_btn_otmena)\

yes = InlineKeyboardButton("Есть", callback_data='yes1')
no = InlineKeyboardButton("Нет", callback_data='no1')
bzc = InlineKeyboardButton("Будет заключен до сделки", callback_data='bzc1')

bra1 = InlineKeyboardMarkup().row(yes)\
    .row(no)\
    .row(bzc)

work = InlineKeyboardButton("Работает", callback_data='work1')
nowork = InlineKeyboardButton("Не работает", callback_data='nowork1')
pen = InlineKeyboardButton("На пенсии", callback_data='pen1')

cosual_c1 = InlineKeyboardMarkup().row(work)\
    .row(nowork)\
    .row(pen)


kom = InlineKeyboardButton("Коммерческая", callback_data='kom1')
byd = InlineKeyboardButton("Бюджетная", callback_data='byd1')
cvoy_buz = InlineKeyboardButton("Свой бизнес", callback_data='cdoy_buz1')
naym = InlineKeyboardButton("По найму", callback_data='naym1')
pencioner = InlineKeyboardButton("Пенсионер", callback_data='pencioner1')
ip = InlineKeyboardButton("ИП", callback_data='ip1')

zan1 = InlineKeyboardMarkup().row(kom)\
    .row(byd)\
    .row(cvoy_buz)\
    .row(naym)\
    .row(pencioner)\
    .row(ip)\
    .row(inline_btn_otmena)\
















fin = InlineKeyboardMarkup().row(inline_btn_fin)


card_m = InlineKeyboardMarkup().row(inline_btn_down).row(inline_btn_vvesti)


zan = InlineKeyboardMarkup().row(inline_btn_kom)\
    .row(inline_btn_byd)\
    .row(inline_btn_cvoy_buz)\
    .row(inline_btn_naym)\
    .row(inline_btn_pencioner)\
    .row(inline_btn_ip)\
    .row(inline_btn_otmena)\

cosual_c = InlineKeyboardMarkup().row(inline_btn_work)\
    .row(inline_btn_nowork)\
    .row(inline_btn_pen)





inline_btn_stop = InlineKeyboardButton("ЗАКОНЧИЛ", callback_data='stop')

inline_btn_cor = InlineKeyboardButton("Исправить анкету", callback_data='cor')
inline_btn_cor_c = InlineKeyboardButton("Исправить карточку компании", callback_data='cor_c')

corective = InlineKeyboardMarkup().row(inline_btn_cor)
corective_c = InlineKeyboardMarkup().row(inline_btn_cor, inline_btn_cor_c)

start = InlineKeyboardMarkup().row(inline_btn_start)
otmena = InlineKeyboardMarkup().row(inline_btn_otmena)


pay_d = InlineKeyboardMarkup().row(inline_btn_ndfl)\
    .row(inline_btn_pfr)\
    .row(inline_btn_nd)\
    .row(inline_btn_srp)\
    .row(inline_btn_spfb)\
    .row(inline_btn_vph)\
    .row(inline_btn_notpay)\
    .row(inline_btn_otmena)

osnv = InlineKeyboardMarkup().row(inline_btn_cob)\
    .row(inline_btn_coz)\
    .row(inline_btn_are)\
    .row(inline_btn_voi)\
    .row(inline_btn_jr)\
    .row(inline_btn_com)\
    .row(inline_btn_otmena)

educ = InlineKeyboardMarkup().row(inline_btn_uc)\
    .row(inline_btn_2v)\
    .row(inline_btn_vuc)\
    .row(inline_btn_nv)\
    .row(inline_btn_cz)\
    .row(inline_btn_cr)\
    .row(inline_btn_nuvc)\
    .row(inline_btn_rm)\
    .row(inline_btn_umba)\
    .row(inline_btn_otmena)

fam = InlineKeyboardMarkup().row(inline_btn_jz)\
    .row(inline_btn_gr)\
    .row(inline_btn_hz)\
    .row(inline_btn_raz)\
    .row(inline_btn_vdo)\
    .row(inline_btn_otmena)

bra = InlineKeyboardMarkup().row(inline_btn_yes)\
    .row(inline_btn_no)\
    .row(inline_btn_bzc)\
    .row(inline_btn_otmena)






continue_menu = InlineKeyboardMarkup().row(inline_btn_stop).row(inline_btn_otmena)

