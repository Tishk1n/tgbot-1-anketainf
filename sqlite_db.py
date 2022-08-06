import sqlite3
import time
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    #_____________________________Добавление юзера_________________________--
    def examination(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(res))

    def add(self, user_id):
        with self.connection:
            return self.connection.execute("INSERT INTO users ('user_id') VALUES (?)", (user_id,))

    # _____________________________Активация анкеты_________________________--

    def user_anketa(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT anketa FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            print(res)
            return int(res[0][0])

    def add_anketa(self, user_id, anketa):
        with self.connection:
            return self.cursor.execute("UPDATE users SET anketa = ? WHERE user_id = ?", (anketa, user_id))

    def user_pay_d(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT pay_d FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_pay_d(self, user_id, pay_d):
        with self.connection:
            return self.cursor.execute("UPDATE users SET pay_d = ? WHERE user_id = ?", (pay_d, user_id))

    def user_adres(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT adres FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_adres(self, user_id, adres):
        with self.connection:
            return self.cursor.execute("UPDATE users SET adres = ? WHERE user_id = ?", (adres, user_id))

    def user_time_live(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT time_live FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_time_live(self, user_id, time_live):
        with self.connection:
            return self.cursor.execute("UPDATE users SET time_live = ? WHERE user_id = ?", (time_live, user_id))

    def user_osnovanie(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT osnovanie FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_osnovanie(self, user_id, osnovanie):
        with self.connection:
            return self.cursor.execute("UPDATE users SET osnovanie = ? WHERE user_id = ?", (osnovanie, user_id))

    def user_education(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT education FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_education(self, user_id, education):
        with self.connection:
            return self.cursor.execute("UPDATE users SET education = ? WHERE user_id = ?", (education, user_id))

    def user_family(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT family FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_family(self, user_id, family):
        with self.connection:
            return self.cursor.execute("UPDATE users SET family= ? WHERE user_id = ?", (family, user_id))

    def user_brak(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT brak FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_brak(self, user_id, brak):
        with self.connection:
            return self.cursor.execute("UPDATE users SET brak= ? WHERE user_id = ?", (brak, user_id))


    def user_cosual(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT cosual FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_cosual(self, user_id, cosual):
        with self.connection:
            return self.cursor.execute("UPDATE users SET cosual= ? WHERE user_id = ?", (cosual, user_id))

    def user_e_mail(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT e_mail FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_e_mail(self, user_id, e_mail):
        with self.connection:
            return self.cursor.execute("UPDATE users SET e_mail= ? WHERE user_id = ?", (e_mail, user_id))

    def user_phone_number(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT phone_number FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_phone_number(self, user_id, phone_number):
        with self.connection:
            return self.cursor.execute("UPDATE users SET phone_number= ? WHERE user_id = ?", (phone_number, user_id))

    def user_cnulc(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT cnulc FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_cnulc(self, user_id, cnulc):
        with self.connection:
            return self.cursor.execute("UPDATE users SET cnulc= ? WHERE user_id = ?", (cnulc, user_id))

    def user_zan(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT zan FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_zan(self, user_id, zan):
        with self.connection:
            return self.cursor.execute("UPDATE users SET zan= ? WHERE user_id = ?", (zan, user_id))

    def user_card(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT card FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_card(self, user_id, card):
        with self.connection:
            return self.cursor.execute("UPDATE users SET card= ? WHERE user_id = ?", (card, user_id))



    #_____________________________COMPANY___________________________

    def examination_com(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM down_card WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(res))

    def add_com(self, user_id):
        with self.connection:
            return self.connection.execute("INSERT INTO down_card ('user_id') VALUES (?)", (user_id,))

    def user_name(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT name FROM down_card WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE down_card SET name= ? WHERE user_id = ?", (name, user_id))

    def user_adres_company(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT adres_company FROM down_card WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_adres_company(self, user_id, adres_company):
        with self.connection:
            return self.cursor.execute("UPDATE down_card SET adres_company= ? WHERE user_id = ?", (adres_company, user_id))

    def user_years(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT years FROM down_card WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_years(self, user_id, years):
        with self.connection:
            return self.cursor.execute("UPDATE down_card SET years= ? WHERE user_id = ?", (years, user_id))

    def user_sait(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT saits FROM down_card WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_saits(self, user_id, sait):
        with self.connection:
            return self.cursor.execute("UPDATE down_card SET saits= ? WHERE user_id = ?", (sait, user_id))

    def user_number_com(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT number_com FROM down_card WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_number_com(self, user_id, number_com):
        with self.connection:
            return self.cursor.execute("UPDATE down_card SET number_com= ? WHERE user_id = ?", (number_com, user_id))

    def user_count(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT count FROM down_card WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_count(self, user_id, count):
        with self.connection:
            return self.cursor.execute("UPDATE down_card SET count= ? WHERE user_id = ?", (count, user_id))

    def user_cfera(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT cfera FROM down_card WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_cfera(self, user_id, cfera):
        with self.connection:
            return self.cursor.execute("UPDATE down_card SET cfera= ? WHERE user_id = ?", (cfera, user_id))

    #______________________________________________________________________________________


    def user_start_work(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT start_work FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_start_work(self, user_id, start_work):
        with self.connection:
            return self.cursor.execute("UPDATE users SET start_work= ? WHERE user_id = ?", (start_work, user_id))

    def user_start_work2(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT start_work2 FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_start_work2(self, user_id, start_work2):
        with self.connection:
            return self.cursor.execute("UPDATE users SET start_work2= ? WHERE user_id = ?", (start_work2, user_id))

    def user_dolg(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT dolg FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_dolg(self, user_id, dolg):
        with self.connection:
            return self.cursor.execute("UPDATE users SET dolg= ? WHERE user_id = ?", (dolg, user_id))

    def user_dohod(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT dohod FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_dohod(self, user_id, dohod):
        with self.connection:
            return self.cursor.execute("UPDATE users SET dohod= ? WHERE user_id = ?", (dohod, user_id))

    def user_dohod2(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT dohod2 FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_dohod2(self, user_id, dohod2):
        with self.connection:
            return self.cursor.execute("UPDATE users SET dohod2= ? WHERE user_id = ?", (dohod2, user_id))

    def user_credit(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT credit FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_credit(self, user_id, credit):
        with self.connection:
            return self.cursor.execute("UPDATE users SET credit= ? WHERE user_id = ?", (credit, user_id))

    def user_credit_card(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT credit_card FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_credit_card(self, user_id, credit_card):
        with self.connection:
            return self.cursor.execute("UPDATE users SET credit_card= ? WHERE user_id = ?", (credit_card, user_id))

    def user_limi(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT limi FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_limi(self, user_id, limi):
        with self.connection:
            return self.cursor.execute("UPDATE users SET limi= ? WHERE user_id = ?", (limi, user_id))

    def user_car(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT car FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_car(self, user_id, car):
        with self.connection:
            return self.cursor.execute("UPDATE users SET car= ? WHERE user_id = ?", (car, user_id))

    def user_cob(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT cob FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_cob(self, user_id, cob):
        with self.connection:
            return self.cursor.execute("UPDATE users SET cob= ? WHERE user_id = ?", (cob, user_id))



