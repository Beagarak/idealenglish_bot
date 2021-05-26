## Функции взаимодействия с базой данных
#
#  Реализует соединение с базой данных и обращение к ней
#  @file bd.py
#  @author Титова Екатерина

import mysql.connector
from mysql.connector import errorcode
import sys
import settings

## Подключаемся к базе данных

try:
    db = mysql.connector.connect(
        host=settings.bd_host,
        user=settings.bd_user,
        passwd=settings.bd_passwd,
        database=settings.bd_database
    )

## Обработка ошибок при подключении

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Try again")
        sys.exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
        sys.exit()
    else:
        print(err)
        sys.exit()

cursor = db.cursor()


## Функция добавления слов в базу данных
#  @param user_words: Список из двух слов (1-английское, 2-русское)
#  @param user_id: Id пользователя в телеграм
#  @return Добавляет слова в безу данных
def add_to_db(user_words, user_id):
    eng_word, rus_word = [i.strip() for i in user_words.split('.')]
    sql = "INSERT INTO words (eng_word, rus_word, user_id) VALUES (%s, %s, %s)"
    val = (eng_word.lower(), rus_word.lower(), user_id)
    cursor.execute(sql, val)
    db.commit()


## Функция получения из базы данных случайной пары слово-перевод по id
#  @param user_id: Id пользователя в телеграм
#  @return Список из двух слов (1-английское, 2-русское)
def take_user_words(user_id):
    query = "SELECT eng_word, rus_word FROM words WHERE user_id=" + str(
        user_id) + " " + "ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    trash = cursor.fetchall()
    list_of_words = [trash[0][0], trash[0][1]]
    return list_of_words


## Функция получения из базы данных случайной пары слово-перевод из всей таблицы
#  @return Список из двух слов (1-английское, 2-русское)
def take_other_words():
    query = "SELECT eng_word, rus_word FROM words ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    trash = cursor.fetchall()
    random_words = [trash[0][0], trash[0][1]]
    return random_words


## Функция получения из базы данных случайной 5 пар слово-перевод по id
#  @param user_id: Id пользователя в телеграм
#  @return 5 строк формата (английское слово - русский перевод)
def words_to_learn(user_id):
    query = "SELECT eng_word, rus_word FROM words WHERE user_id=" + str(
        user_id) + " " + "ORDER BY RAND() LIMIT 5"
    cursor.execute(query)
    trash = cursor.fetchall()
    result = ''
    for a, b in trash:
        result += '{} - {}\n'.format(a, b)
    return result


## Функция пороверки наличия слова в базе данных по id пользователя
#  @param user_id: Id пользователя в телеграм
#  @param text: слово на английском, по которому осуществляется поиск
#  @return количество строк, в котором записано эт слово для данного id
def count_if_exists(user_id, text):
    query = "SELECT COUNT(*) FROM words WHERE user_id=" + str(user_id) + " and eng_word='" + str(text) + "'"
    cursor.execute(query)
    trash = cursor.fetchall()
    result = ''
    for a in trash:
        result += '{}'.format(a)
    return int(result[1])


