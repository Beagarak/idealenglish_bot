from translate import Translator
import telebot

bot = telebot.TeleBot('1601838792:AAFCSBGDVasuRk10nWDZYcZ9nz5noB-GqtM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    type_of_lang = int(ord(message.text[0]))
    if 1103 >= type_of_lang >= 1040:
        translator = Translator(from_lang='Russian', to_lang='English')
        translation = translator.translate(message.text)
        translation = translation.split('&')[0]  # отсекаем мусор, который иногда появляется
        bot.send_message(message.from_user.id, translation)
    elif 122 >= type_of_lang >= 65:
        translator = Translator(from_lang='English', to_lang='Russian')
        translation = translator.translate(message.text)
        bot.send_message(message.from_user.id, translation)


bot.polling(none_stop=True, interval=0)