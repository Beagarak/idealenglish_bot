## Функции для работы переводчика
#
# Реализует операции перевода слов
# @file trans_alg.py
# @author Есаулов Лев

from translate import Translator
import telebot
from settings import TG_TOKEN
import buttons

bot = telebot.TeleBot(TG_TOKEN)


## Обрабатывает слово(или текст) для перевода
# @param asci Аски код первого символа текста, который мы должны перевести
# @param text Слово(или текст), который мы должны перевести
# @return Возвращает список слов длинной 3, где первое слово - англ., второе - русс., третье - переведенное слово
def get_translate(asci, text):
    trans_and_lang = []
    trans_and_lang.clear()
    translation = ''
    if 1103 >= asci >= 1040:
        translator = Translator(from_lang='Russian', to_lang='English')
        translation = translator.translate(text)
        trans_and_lang.append(translation)
        trans_and_lang.append(text)
        translation = translation.split('&')[0]  # отсекаем мусор
    elif 122 >= asci >= 65:
        translator = Translator(from_lang='English', to_lang='Russian')
        translation = translator.translate(text)
        trans_and_lang.append(text)
        trans_and_lang.append(translation)
    trans_and_lang.append(translation)
    return trans_and_lang


## Находит картинку через "Яндекс"
# @param text Слово(или текст) полученное от пользователя
# @return Возвращает ссылку на картинку
def get_picture(text):
    link = 'https://yandex.ru/images/search?text=' + text.lower() + '%20'
    return link


## Обрабатывает слово(или текст) и отправляет его перевод с картинкой пользователю
# @param user_word Слово(или текст) полученное от пользователя
# @param user_id Адрес пользователя, на который посылаем сообщение
# @return возвращает Список из англ и русского слова
def translation_function(user_word, user_id):
    type_of_lang = int(ord(user_word[0]))
    log_words = get_translate(type_of_lang, user_word)
    translation = log_words[2]
    log_words.pop(2)
    log_words = str(log_words[0]) + '.' + str(log_words[1])
    bot.send_message(user_id, translation)
    bot.send_photo(chat_id=user_id,
                   photo=get_picture(translation))
    buttons.TranslateButtons(user_id).creating_translate_keyboard(user_id)
    return log_words
