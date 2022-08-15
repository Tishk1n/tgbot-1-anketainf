import json

from tortoise import fields

from bot.database.models.abstract_base import AbstractBaseModel


class User(AbstractBaseModel):
    id_tg = fields.BigIntField(null=False, unique=True)
    photos = fields.CharField(max_length=3000)
    income = fields.CharField(max_length=200)
    fact_address = fields.CharField(max_length=300)
    time_this = fields.CharField(max_length=200)
    address = fields.CharField(max_length=200)
    study = fields.CharField(max_length=200)
    material_status = fields.CharField(max_length=200)
    marriage = fields.CharField(max_length=200, null=True)
    social = fields.CharField(max_length=200, null=True)
    email = fields.CharField(max_length=200)
    phone = fields.CharField(max_length=200)
    snils = fields.CharField(max_length=200)
    busyness_type = fields.CharField(max_length=200)
    card_company = fields.CharField(max_length=200)
    start_time_work = fields.CharField(max_length=200)
    full_name = fields.CharField(max_length=200)
    address_company = fields.CharField(max_length=200)
    site = fields.CharField(max_length=200)
    phone_company = fields.CharField(max_length=200)
    first_work = fields.CharField(max_length=200)
    post = fields.CharField(max_length=200)
    main_income = fields.CharField(max_length=200)
    back_income = fields.CharField(max_length=200)
    credit_count = fields.CharField(max_length=200, null=True)
    credit_card = fields.CharField(max_length=200, null=True)
    limit_card = fields.CharField(max_length=200, null=True)
    car = fields.CharField(max_length=200, null=True)
    property = fields.CharField(max_length=200)

    def to_str(self) -> str:
        return f'<b>Фото паспорта</b>: {json.loads(self.photos)},\n' \
               f'<b>Способ подтверждения дохода</b>: {self.income}\n' \
               f'<b>Адрес фактического проживания</b>: {self.fact_address}\n' \
               f'<b>Проживаете по этому адресу</b>: {self.time_this}\n' \
               f'<b>Основание проживания</b>: {self.address}\n' \
               f'<b>Образование</b>: {self.study}\n' \
               f'<b>Семейное положение</b>: {self.material_status}\n' \
               f'<b>Брачный контракт</b>: {self.marriage}\n' \
               f'<b>Социальный статус супруга(-и)</b>: {self.social}\n' \
               f'<b>Электронная почта</b>: {self.email}\n' \
               f'<b>Номер телефона</b>: {self.phone}\n' \
               f'<b>Номер СНИЛС</b>: {self.snils}\n' \
               f'<b>Тип занятости</b>: {self.busyness_type}\n' \
               f'<b>Карточка компании</b>: {self.card_company}\n' \
               f'<b>Дата начала работы в указанной организации</b>: {self.start_time_work}\n' \
               f'<b>Полное наименование компании</b>: {self.full_name}\n' \
               f'<b>Фактический адрес компании</b>: {self.address_company}\n' \
               f'<b>Сайт компании</b>: {self.site}\n' \
               f'<b>Номер телефона компании</b>: {self.phone_company}\n' \
               f'<b>Дата начала своей трудовой деятельности</b>: {self.first_work}\n' \
               f'<b>Название должности</b>: {self.post}\n' \
               f'<b>Основной доход в месяц в рублях</b>: {self.main_income}\n' \
               f'<b>Дополнительный доход в месяц</b>: {self.back_income}\n' \
               f'<b>Сумма выплат на  погашение кредитов</b>: {self.credit_count}\n' \
               f'<b>Сколько кредитных карт</b>: {self.credit_card}\n' \
               f'<b>Месячный лимит каждой карты через запятую</b>: {self.limit_card}\n' \
               f'<b>Автомобиль\и</b>: {self.car}\n' \
               f'<b>Недвижимость\и</b>: {self.property}\n'

    class Meta:
        table = 'users'
