import telebot
from settings import TG_TOKEN
import trans_alg
import buttons

bot = telebot.TeleBot(TG_TOKEN)
status = 0


@bot.message_handler(commands=['start'])
def handle_start(message):
    buttons.main_menu(message)


@bot.message_handler(content_types=['text'])
def basic_actions(message):
    global status
    if status == 1:
        if change_status(message) == 1:
            pass
    elif status == 2:
        if change_status(message) == 1:
            pass
    elif status == 3:
        if change_status(message) == 1:
            pass
    elif status == 4:
        # Если не нажали никакую кнопку, то переводим.
        if change_status(message) == 1:
            translate(message)
    elif status == 5:
        if change_status(message) == 1:
            pass
    else:
        if change_status(message) == 1:
            bot.send_message(message.from_user.id,
                             'Не понимаю, используй клавиатуру')


@bot.message_handler(content_types=['text'])
def translate(message):
    type_of_lang = int(ord(message.text[0]))
    translation = trans_alg.get_translate(type_of_lang, message.text)
    bot.send_message(message.from_user.id, translation)
    bot.send_photo(chat_id=message.chat.id, photo=trans_alg.get_picture(translation))


@bot.message_handler(content_types=['text'])
def change_status(message):
    global status
    if message.text == buttons.add_word_button:
        status = 1
        bot.send_message(message.from_user.id,
                         'Можешь добавить своё слово! (в разработке)')
        return 0
    elif message.text == buttons.check_knowledge_button:
        status = 2
        bot.send_message(message.from_user.id,
                         'Пора проверить твои знания (в разработке)')
        return 0
    elif message.text == buttons.learn_words_button:
        status = 3
        bot.send_message(message.from_user.id,
                         'Давай поучим новые слова! (в разработке)')
        return 0
    elif message.text == buttons.translate_button:
        status = 4
        bot.send_message(message.from_user.id,
                         'Введи слово, которое хочешь перевести:')
        return 0
    elif message.text == buttons.statistic_button:
        status = 5
        bot.send_message(message.from_user.id,
                         'Вот твоя статистика: (в разработке)')
    else:
        return 1


bot.polling(none_stop=True, interval=0)