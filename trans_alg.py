from translate import Translator
import telebot
from settings import TG_TOKEN
import buttons

bot = telebot.TeleBot(TG_TOKEN)


def get_translate(asci, text):
    """
    :param asci: Аски код первого символа текста, который мы должны перевести
    :param text: Слово(или текст), который мы должны перевести
    :return: Список слов длинной 3, где первое слово - англ., второе - русс., третье - переведенное слово
    """
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


def get_picture(text):
    """
    :param text: Слово(или текст), который мы должны перевести
    :return: Картинка, которая показывает, что означет слово
    """
    link = 'https://yandex.ru/images/search?text=' + text.lower() + '%20'
    return link


def translation_function(user_word, user_id):
    """
    :param user_word: Слово(или текст) полученное от пользователя
    :param user_id: адрес пользователя, на который посылаем сообщение
    :return: Отправляет переведенное слово и картинку пользователю
    """
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