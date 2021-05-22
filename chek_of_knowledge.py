import random
import mysql.connector
from mysql.connector import errorcode
import sys

import buttons
import settings
from settings import TG_TOKEN
import telebot

bot = telebot.TeleBot(TG_TOKEN)
user__id = 739414278

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


def take_user_words(user_id):
    query = "SELECT eng_word, rus_word FROM words WHERE user_id=" + str(
        user_id) + " " + "ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    trash = cursor.fetchall()
    list_of_words = [trash[0][0], trash[0][1]]
    return list_of_words


def take_other_words():
    query = "SELECT eng_word, rus_word FROM words ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    trash = cursor.fetchall()
    random_words = [trash[0][0], trash[0][1]]
    return random_words


eng_user_word = ''
eng_random_word = ''
eng_inform1 = ''
eng_inform2 = ''
rus_user_word = ''
rus_random_word = ''
rus_inform1 = ''
rus_inform2 = ''


def eng_rus_quiz(list_of_words, random_words, call):
    global eng_user_word, eng_random_word, eng_inform1, eng_inform2
    eng_user_word = list_of_words[1]
    eng_random_word = random_words[1]
    inform = 'Выберите перевод для слова: ' + list_of_words[0]
    eng_inform1 = 'Супер'
    eng_inform2 = 'Вы ошиблись, правильный перевод: ' + list_of_words[1]
    bot.send_message(call.from_user.id, inform)
    buttons.EngQuizButtons(call).creating_keyboard(call)


def rus_eng_quiz(list_of_words, random_words, call):
    global rus_user_word, rus_random_word, rus_inform1, rus_inform2
    rus_user_word = list_of_words[0]
    rus_random_word = random_words[0]
    inform = 'Выберите перевод для слова: ' + list_of_words[1]
    rus_inform1 = 'Супер'
    rus_inform2 = 'Вы ошиблись, правильный перевод: ' + list_of_words[0]
    bot.send_message(call.from_user.id, inform)
    buttons.RusQuizButtons(call).creating_keyboard(call)



def mixer(word):
    letters = list(word)
    random.shuffle(letters)
    return letters


def rus_eng_letters(list_of_words, call):
    trash = ' '.join(mixer(list_of_words[0]))
    inform = 'Соберите слово: ' + list_of_words[1] + ' из букв:' + '\n' + trash
    bot.send_message(call.from_user.id, inform)

    @bot.message_handler(content_types=['text'])
    def rus_eng_check_answer(message):
        if list_of_words[0].lower() == message:
            bot.send_message(message.from_user.id, 'Правильно!')
        else:
            bot.send_message(message.from_user.id, 'К сожалению, неправильно')


def eng_rus_letters(list_of_words, call):
    trash = ' '.join(mixer(list_of_words[1]))
    inform = 'Соберите слово: ' + list_of_words[0] + ' из букв:' + '\n' + trash
    bot.send_message(call.from_user.id, inform)

    @bot.message_handler(content_types=['text'])
    def eng_rus_check_answer(message):
        if list_of_words[1].lower() == message:
            bot.send_message(message.from_user.id, 'Правильно!')
        else:
            bot.send_message(message.from_user.id, 'К сожалению, неправильно')


# функция 5
# тут используется take_random_rus_word
#
#
# def game_5(list_of_words):
#     print('Выберите режим:')
#     x = input()
#     mode = 0
#     if x == 'РА':
#         mode = 2
#     elif x == 'АР':
#         mode = 1
#
#     if mode == 1:
#         print(list_of_words[0], 'Укажите перевод:', sep='\n')
#         y = input()
#         if list_of_words[1].lower() == y.lower():
#             print('Супер')
#         else:
#             print('Вы ошиблись, правильный перевод', list_of_words[1])
#     elif mode == 2:
#         print(list_of_words[1], 'Укажите перевод:', sep='\n')
#         y = input()
#         if list_of_words[0].lower() == y.lower():
#             print('Супер')
#         else:
#             print('Вы ошиблись, правильный перевод', list_of_words[0])
#     else:
#         print('Неверный режим')
#
#
# game_5(take_random_rus_word(user_id))
