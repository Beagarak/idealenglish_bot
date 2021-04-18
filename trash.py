# bot.send_photo(ид_получателя, 'https://example.org/адрес/картинки.jpg');
import telebot
from glob import glob
from random import choice

bot = telebot.TeleBot('1601838792:AAFCSBGDVasuRk10nWDZYcZ9nz5noB-GqtM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'яблоко':
        bot.send_message(message.from_user.id, 'Apple')
        bot.send_photo(chat_id=message.chat.id, photo='https://www.healthbenefitstimes.com/9/gallery/apple-1/Half'
                                                      '-cut-apple.jpg')
    else:
        bot.send_message(message.from_user.id, 'Напишите "яблоко"!')


bot.polling(none_stop=True, interval=0)
