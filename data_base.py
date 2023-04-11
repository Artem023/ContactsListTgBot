import sqlite3
from constants import GREETING_MESSAGE


# Таблица с id юзеров в телеграме
# Можно добавит инлайн кнопки для продолжения работы
# Можно передавать имя юзера

def db_start():
    db = sqlite3.connect('new_contact.db')
    cur = db.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users_ids (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE NOT NULL
        )''')

    db.commit()


def creat_users_id(tg_user_id: int) -> str:
        with sqlite3.connect('new_contact.db') as db:
            cur = db.cursor()

        try:
            user = cur.execute("SELECT user_id FROM users_ids WHERE user_id == '{key}'".format(key=tg_user_id)).fetchone()
            if user is None:
                cur.execute("INSERT INTO users_ids (user_id) VALUES ('{key}')".format(key=tg_user_id))
                db.commit()
                return GREETING_MESSAGE

            else:
                return "Снова здравствуйте! Начнем работу."

        except sqlite3.Error as err:
            return f"Error: {err}. Что-то пошло не так. Попробуйте еще раз!"

        finally:
            cur.close()
            db.close()




