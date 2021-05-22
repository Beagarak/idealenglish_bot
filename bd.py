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


def add_to_db(user_words, user_id):
    """
    :param user_words: Two-word list(1-eng, 2-rus)
    :param user_id: User_id in the tg
    :return: Adds words to the database
    """
    eng_word, rus_word = [i.strip() for i in user_words.split('.')]
    sql = "INSERT INTO words (eng_word, rus_word, user_id) VALUES (%s, %s, %s)"
    val = (eng_word, rus_word, user_id)
    cursor.execute(sql, val)
    db.commit()
