from translate import Translator
import telebot
from settings import TG_TOKEN
import buttons

bot = telebot.TeleBot(TG_TOKEN)


def get_translate(asci, text):
    trans_and_lang = []
    trans_and_lang.clear()
    translation = ''
    if 1103 >= asci >= 1040:
        translator = Translator(from_lang='Russian', to_lang='English')
        translation = translator.translate(text)
        trans_and_lang.append(translation)
        trans_and_lang.append(text)
        translation = translation.split('&')[
            0]  # отсекаем мусор, который иногда появляется
    elif 122 >= asci >= 65:
        translator = Translator(from_lang='English', to_lang='Russian')
        translation = translator.translate(text)
        trans_and_lang.append(text)
        trans_and_lang.append(translation)
    trans_and_lang.append(translation)
    return trans_and_lang


def get_picture(text):
    link = 'https://yandex.ru/images/search?text=' + text.lower() + '%20'
    return link


def translation_function(message):
    type_of_lang = int(ord(message.text[0]))
    log_words = get_translate(type_of_lang, message.text)
    translation = log_words[2]
    log_words.pop(2)
    bot.send_message(message.from_user.id, translation)
    bot.send_photo(chat_id=message.chat.id,
                   photo=get_picture(translation))
    buttons.LocalButtons(message).creating_keyboard(message)
    log_user_id = message.chat.id
    log_theme = "default"
    bd.add_to_db_from_translator(log_words, log_theme, log_user_id)
