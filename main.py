import telebot
from settings import TG_TOKEN
import trans_alg
import buttons


bot = telebot.TeleBot(TG_TOKEN)



@bot.message_handler(content_types=['text'])
def translator(message):
    type_of_lang = int(ord(message.text[0]))
    translation = trans_alg.get_translate(type_of_lang, message.text)
    bot.send_message(message.from_user.id, translation)
    bot.send_photo(chat_id=message.chat.id, photo=trans_alg.get_picture(translation))

    
@bot.message_handler(commands=['start'])
def handle_start(message):
    buttons.main_menu(message)


@bot.message_handler(content_types=['text'])
def basic_actions(message):
    if message.text == buttons.add_word_button:
        bot.send_message(message.from_user.id,
                         'Можешь добавить своё слово! (в разработке)')
    elif message.text == buttons.check_knowledge_button:
        bot.send_message(message.from_user.id,
                         'Пора проверить твои знания (в разработке)')
    elif message.text == buttons.learn_words_button:
        bot.send_message(message.from_user.id,
                         'Давай поучим новые слова! (в разработке)')
    elif message.text == buttons.translate_button:
        bot.send_message(message.from_user.id,
                         'Введи слово, которое хочешь перевести:')
    elif message.text == buttons.statistic_button:
        bot.send_message(message.from_user.id,
                         'Вот твоя статистика: (в разработке)')
    else:
        bot.send_message(message.from_user.id,
                         'Не понимаю, используй клавиатуру')


bot.polling(none_stop=True, interval=0)
