import mysql.connector
from mysql.connector import errorcode
import sys
import settings

try:
    db = mysql.connector.connect(
        host=settings.bd_host,
        user=settings.bd_user,
        passwd=settings.bd_passwd,
        database=settings.bd_database
    )
<<<<<<< HEAD

=======
>>>>>>> 8cffff85d72f507515f2f96bb55b44cf420d7504
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


#####################################
# показывает все созданные таблицы
# cursor.execute("SHOW TABLES")
# for x in cursor:
#   print(x)

#####################################
# создание таблицы

# cursor.execute("CREATE TABLE words (id INT AUTO_INCREMENT PRIMARY KEY, eng_word VARCHAR(255), rus_word VARCHAR(255),"
#                "theme VARCHAR(255), user_id INT(11))")

#####################################
# запись данных

# sql = "INSERT INTO words (eng_word, rus_word, theme, user_id) VALUES (%s, %s, %s, %s)"
# val = [
#     ("apple", "яблоко", "fruits", 123456789),
#     ("peach", "персик", "other fruits", 123456789),
#     ("dog", "собака", "animals", 123456789),
#     ("banana", "банан", "fruits", 123456788),
#     ("cat", "кот", "animals", 123456787),
# ]
#
# cursor.executemany(sql, val)
# db.commit()

#####################################
# вывод всей таблицы

# cursor.execute("SELECT * FROM words")
# result = cursor.fetchall()
# for x in result:
#   print(x)

#####################################
# вывод некоторых столбцов

# cursor.execute("SELECT eng_word, rus_word FROM words")
# result = cursor.fetchall()
# for x in result:
#   print(x)

#####################################
# выбор перевода слова "apple" для пользователя 123456789

# cursor.execute("SELECT rus_word FROM words WHERE eng_word='apple' and user_id='123456789'")
# result = cursor.fetchall()
# for x in result:
#   print(x)

#####################################
# добавление одной строки в бд


def add_to_db(user_words, user_id):
<<<<<<< HEAD
=======
    """
    :param user_words: Two-word list(1-eng, 2-rus)
    :param user_id: User_id in the tg
    :return: Adds words to the database
    """

>>>>>>> 8cffff85d72f507515f2f96bb55b44cf420d7504
    eng_word, rus_word = [i.strip() for i in user_words.split('.')]
    sql = "INSERT INTO words (eng_word, rus_word, user_id) VALUES (%s, %s, %s)"
    val = (eng_word, rus_word, user_id)
    cursor.execute(sql, val)
    db.commit()


#####################################
# удаление всех строк где есть слово "apple"

# sql = "DELETE FROM words WHERE eng_word = %s"
# val = ("banana", )
# cursor.execute(sql, val)
# db.commit()
# print('Запись удалена!')

######################################
# удаление конкретной строки со словом "apple" по id пользователя

# sql = "DELETE FROM words WHERE eng_word = %s AND user_id = %s"
# val = ("apple", 123456789)
# cursor.execute(sql, val)
# db.commit()
# print('Запись удалена!')
######################################
<<<<<<< HEAD

# cursor.execute("CREATE DATABASE bot")
=======
>>>>>>> 8cffff85d72f507515f2f96bb55b44cf420d7504
