import sqlite3

db_file = "db.db"
def create_all(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    with connection:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY, 
                user_id INTEGER, 
                anketa INTEGER DEFAULT 0 NOT NULL, 
                pay_d TEXT, 
                adres TEXT, 
                time_live TEXT, 
                osnovanie TEXT, 
                education TEXT, 
                family TEXT, 
                brak TEXT, 
                cosual TEXT, 
                e_mail TEXT, 
                phone_number TEXT, 
                cnulc TEXT, 
                zan TEXT, 
                card TEXT,
                start_work TEXT,
                start_work2 TEXT,
                dolg TEXT,
                dohod TEXT,
                dohod2 TEXT,
                credit TEXT,
                credit_card TEXT,
                limi TEXT,
                car TEXT,
                cob TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS down_card (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                name TEXT,
                adres_company TEXT,
                years TEXT,
                saits TEXT,
                number_com TEXT,
                count TEXT,
                cfera TEXT
            )
        """)

def test(db_file):
    db = Database(db_file)
    db.add(0)
    print(db.examination(0))

    db.add_anketa(0, 0)
    print(db.user_anketa(0))

    db.add_pay_d(0, "pay_d")
    print(db.user_pay_d(0))

    db.add_adres(0, "adress")
    print(db.user_adres(0))

    db.add_time_live(0, "time_live")
    print(db.user_time_live(0))

    db.add_osnovanie(0, "osnovanie")
    print(db.user_osnovanie(0))

    db.add_education(0, "education")
    print(db.user_education(0))

    db.add_family(0, "family")
    print(db.user_family(0))

    db.add_brak(0, "user_brak")
    print(db.user_brak(0))

    db.add_cosual(0, "cosual")
    print(db.user_cosual(0))
    
    db.add_e_mail(0, "e_mail")
    print(db.user_e_mail(0))
    
    db.add_phone_number(0, "phone_number")
    print(db.user_phone_number(0))

    db.add_cnulc(0, "cnulc")
    print(db.user_cnulc(0))

    db.add_zan(0, "zan")
    print(db.user_zan(0))

    db.add_card(0, "card")
    print(db.user_card(0))

    db.add_com(0)
    print(db.examination_com(0))

    db.add_name(0, "name")
    print(db.user_name(0))

    db.add_adres_company(0, "adres_company")
    print(db.user_adres_company(0))

    db.add_years(0, "years")
    print(db.user_years(0))

    db.add_saits(0, "saits")
    print(db.user_sait(0))

    db.add_number_com(0, "number_com")
    print(db.user_number_com(0))

    db.add_count(0, "count")
    print(db.user_count(0))

    db.add_cfera(0, "cfera")
    print(db.user_cfera(0))

    db.add_start_work(0, "start_work")
    print(db.user_start_work(0))

    db.add_start_work2(0, "start_work2")
    print(db.user_start_work2(0))

    db.add_dolg(0, "dolg")
    print(db.user_dolg(0))

    db.add_dohod(0, "dohod")
    print(db.user_dohod(0))

    db.add_dohod2(0, "dohod2")
    print(db.user_dohod2(0))

    db.add_credit(0, "credit")
    print(db.user_credit(0))

    db.add_credit_card(0, "credit_card")
    print(db.user_credit_card(0))

    db.add_limi(0, "limi")
    print(db.user_limi(0))

    db.add_car(0, "car")
    print(db.user_car(0))

    db.add_cob(0, "cob")
    print(db.user_cob(0))

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


if __name__ == '__main__':
    create_all(db_file)
    #test(db_file)