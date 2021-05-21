from translate import Translator
import telebot
from settings import TG_TOKEN
import buttons

# import bd

bot = telebot.TeleBot(TG_TOKEN)


def get_translate(asci, text):
    """
    :param asci: Ascii code of the first character of the text that we must to translate
    :param text: The first character of the word(or text) that we must to translate
    :return: a list of words of length 3, where first is english,
    second word is russian and third is translated word(or text).
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
    :param text: The first character of the word(or text) that we must to translate
    :return: A picture that shows our word for translation
    """
    link = 'https://yandex.ru/images/search?text=' + text.lower() + '%20'
    return link


def translation_function(message):
    """
    :param message: Word(or text) received from the user
    :return: Sends the translated word and picture to the user, and also adds the word to the database
    """
    type_of_lang = int(ord(message.text[0]))
    log_words = get_translate(type_of_lang, message.text)
    translation = log_words[2]
    log_words.pop(2)
    log_words = str(log_words[0]) + '.' + str(log_words[1])
    bot.send_message(message.from_user.id, translation)
    bot.send_photo(chat_id=message.chat.id,
                   photo=get_picture(translation))
    buttons.LocalButtons(message).creating_keyboard(message)
    # bd.add_to_db(log_words, message.from_user.id)
