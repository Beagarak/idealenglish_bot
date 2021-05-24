## Функции для проверки знаний
#
# Реализует операции различных игровых режимов
# @file chek_of_knowledge.py
# @author Олейник Александр, Титова Екатерина, Есаулов Лев

import random
import buttons
from settings import TG_TOKEN
import telebot

bot = telebot.TeleBot(TG_TOKEN)
eng_user_word = ''
eng_random_word = ''
eng_inform1 = ''
eng_inform2 = ''
rus_user_word = ''
rus_random_word = ''
rus_inform1 = ''
rus_inform2 = ''


## Посылает пользователю слово на рускком и 2 варианта перевода, из которых нужно выбрать одно
# @param list_of_words: Слово и его перевод, взятые из базы данных
# @param random_words: Случайное слово и его перевод, взятые из базы данных
# @param call: Переменная для связи с пользователем
def rus_eng_quiz(list_of_words, random_words, call):
    global rus_user_word, rus_random_word, rus_inform1, rus_inform2
    rus_user_word = list_of_words[0]
    rus_random_word = random_words[0]
    inform = 'Выберите перевод для слова: ' + list_of_words[1]
    rus_inform1 = 'Супер'
    rus_inform2 = 'Вы ошиблись, правильный перевод: ' + list_of_words[0]
    bot.send_message(call.from_user.id, inform)
    buttons.RusQuizButtons(call).creating_keyboard(call)


## Посылает пользователю слово на английском и 2 варианта перевода, из которых нужно выбрать одно
# @param list_of_words: Слово и его перевод, взятые из базы данных
# @param random_words: Случайное слово и его перевод, взятые из базы данных
# @param call: Переменная для связи с пользователем
def eng_rus_quiz(list_of_words, random_words, call):
    global eng_user_word, eng_random_word, eng_inform1, eng_inform2
    eng_user_word = list_of_words[1]
    eng_random_word = random_words[1]
    inform = 'Выберите перевод для слова: ' + list_of_words[0]
    eng_inform1 = 'Супер'
    eng_inform2 = 'Вы ошиблись, правильный перевод: ' + list_of_words[1]
    bot.send_message(call.from_user.id, inform)
    buttons.EngQuizButtons(call).creating_keyboard(call)


## Перемешивает буквы с лучайном порядке
# @param word: Слово, буквы которого мы должны перемешать
# @return Возвращает список перемешанных букв
def mixer(word):
    letters = list(word)
    random.shuffle(letters)
    return letters


## Показывает пользователю слово на английском и перемешенные буквы перевода
# @param list_of_words: слово и его перевод, взятые из базы данных
# @param call: Переменная для связи с пользователем
# @return Возвращает список из двух слов
def rus_eng_letters(list_of_words, call):
    trash = ' '.join(mixer(list_of_words[0]))
    inform = 'Соберите слово: ' + list_of_words[1] + ' из букв:' + '\n' + trash
    bot.send_message(call.from_user.id, inform)
    return list_of_words


## Показывает пользователю слово на русском и перемешенные буквы перевода
# @param list_of_words: слово и его перевод, взятые из базы данных
# @param call: Переменная для связи с пользователем
# @return Возвращает список из двух слов
def eng_rus_letters(list_of_words, call):
    trash = ' '.join(mixer(list_of_words[1]))
    inform = 'Соберите слово: ' + list_of_words[0] + ' из букв:' + '\n' + trash
    bot.send_message(call.from_user.id, inform)
    return list_of_words


## Сравнивает верный ли перевод слова с русского на английский был получен от пользователя
# @param user_ans: присланный перевод слова пользователем
# @param user_id: адрес пользователя, на который посылаем сообщение
# @param list_of_words: слово и его перевод, взятые из базы данных
# @param message: сообщение, полученное от пользователя
def rus_eng_check_answer(user_ans, user_id, list_of_words, message):
    if list_of_words[0].lower() == user_ans.lower():
        bot.send_message(user_id, 'Правильно!')
    else:
        bot.send_message(user_id,
                         'Вы ошиблись, правильный перевод: ' + list_of_words[0])
    buttons.InGameButtons(message).creating_keyboard(message)


## Сравнивает верный ли перевод слова с русского на английский был получен от пользователя
# @param user_ans: присланный перевод слова пользователем
# @param user_id: адрес пользователя, на который посылаем сообщение
# @param list_of_words: слово и его перевод, взятые из базы данных
# @param message: сообщение, полученное от пользователя
def eng_rus_check_answer(user_ans, user_id, list_of_words, message):
    if list_of_words[1].lower() == user_ans.lower():
        bot.send_message(user_id, 'Правильно!')
    else:
        bot.send_message(user_id,
                         'Вы ошиблись, правильный перевод: ' + list_of_words[1])
    buttons.InGameButtons(message).creating_keyboard(message)


## Присылает пользователю слово на русском
# @param list_of_words: слово и его перевод, взятые из базы данных
# @param call: Переменная для связи с пользователем
# @return Возвращает список из двух слов
def rus_write_translate(list_of_words, call):

    inform = 'Впишите верный перевод слова: ' + '\n' + list_of_words[1]
    bot.send_message(call.from_user.id, inform)
    return list_of_words


## Присылает пользователю слово на английском
# @param list_of_words: слово и его перевод, взятые из базы данных
# @param call: Переменная для связи с пользователем
# @return Возвращает список из двух слов
def eng_write_translate(list_of_words, call):
    inform = 'Впишите верный перевод слова: ' + '\n' + list_of_words[0]
    bot.send_message(call.from_user.id, inform)
    return list_of_words


# Вызов функции для мейна
# chek_of_knowledge.eng_write_translate(chek_of_knowledge.take_user_words(
#                                                     call.from_user.id), call)
