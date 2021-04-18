# bot.send_photo(ид_получателя, 'https://www.healthbenefitstimes.com/9/gallery/apple-1/Half-cut-apple.jpg');
import telebot
from glob import glob
from random import choice
bot = telebot.TeleBot('1601838792:AAFCSBGDVasuRk10nWDZYcZ9nz5noB-GqtM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    lists = glob('img/*')
    picture = choice(lists)
    bot.send_message(message.from_user.id, 'Один из создателей:')
    bot.send_photo(chat_id=message.chat.id, photo=open(picture, 'rb'))


bot.polling(none_stop=True, interval=0)