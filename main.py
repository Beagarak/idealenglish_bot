import telebot
from settings import TG_TOKEN
import trans_alg

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    type_of_lang = int(ord(message.text[0]))
    translation = trans_alg.get_translate(type_of_lang, message.text)
    bot.send_message(message.from_user.id, translation)
    bot.send_photo(chat_id=message.chat.id, photo=trans_alg.get_picture(translation))


bot.polling(none_stop=True, interval=0)
