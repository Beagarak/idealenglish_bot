import telebot
from settings import TG_TOKEN
from translate import Translator

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    type_of_lang = int(ord(message.text[0]))
    if 1103 >= type_of_lang >= 1040:
        translator = Translator(from_lang='Russian', to_lang='English')
        translation = translator.translate(message.text)
        translation = translation.split('&')[0]  # отсекаем мусор, который иногда появляется
        bot.send_message(message.from_user.id, translation)
        bot.send_photo(chat_id=message.chat.id, photo='https://yandex.ru/images/search?text='+translation.lower()+'%20')
    elif 122 >= type_of_lang >= 65:
        translator = Translator(from_lang='English', to_lang='Russian')
        translation = translator.translate(message.text)
        bot.send_message(message.from_user.id, translation)
        bot.send_photo(chat_id=message.chat.id, photo='https://yandex.ru/images/search?text='+translation.lower()+'%20')


bot.polling(none_stop=True, interval=0)