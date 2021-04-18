from translate import Translator
import telebot

bot = telebot.TeleBot('1601838792:AAFCSBGDVasuRk10nWDZYcZ9nz5noB-GqtM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    type_of_lang = int(ord(message.text[0]))
    if 1103 >= type_of_lang >= 1040:
        from_l = 'russian'
        to_l = 'english'
        translator = Translator(from_lang=from_l, to_lang=to_l)
        translation = translator.translate(message.text)
        bot.send_message(message.from_user.id, translation)
    elif 122 >= type_of_lang >= 65:
        from_l = 'english'
        to_l = 'russian'
        translator = Translator(from_lang=from_l, to_lang=to_l)
        translation = translator.translate(message.text)
        bot.send_message(message.from_user.id, translation)


bot.polling(none_stop=True, interval=0)