import telebot

import buttons_v2
from settings import TG_TOKEN
import trans_alg
import buttons

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def show_main_menu(message):
    buttons.main_menu(message)


@bot.callback_query_handler(func=lambda call: call.data == buttons.add_word)
def add_word_function(call=buttons.add_word):
    bot.send_message(call.from_user.id,
                     'Можешь добавить свои слова! (в разработке)')
    buttons_v2.LocalButtons(call)


@bot.callback_query_handler(func=lambda call: call.data == buttons.learn_words)
def learn_word_function(call):
    bot.send_message(call.from_user.id,
                     'Давай поучим новые слова! (в разработке)')


@bot.callback_query_handler(
    func=lambda call: call.data == buttons.check_knowledge)
def check_knowledge_function(call):
    bot.send_message(call.from_user.id,
                     'Пора проверить твои знания (в разработке)')


@bot.callback_query_handler(func=lambda call: call.data == buttons.statistic)
def statistic_function(call=buttons.translate):
    bot.send_message(call.from_user.id, 'Вот твоя статистика: (в разработке)')


@bot.callback_query_handler(func=lambda call: call.data == buttons.translate)
def translator_function(call):
    bot.send_message(call.from_user.id,
                     'Введи слово, которое хочешь перевести:')
    new_keyboard_translator = buttons_v2.LocalButtons(call)

    @bot.message_handler(content_types=['text'])
    def translate(message):
        type_of_lang = int(ord(message.text[0]))
        translation = trans_alg.get_translate(type_of_lang, message.text)
        bot.send_message(message.from_user.id, translation)
        bot.send_photo(chat_id=message.chat.id,
                       photo=trans_alg.get_picture(translation))
        bot.send_message(call.from_user.id, text='Выберите:',
                         reply_markup=new_keyboard_translator)


@bot.callback_query_handler(
    func=lambda call: call.data == buttons.exit_to_main_menu)
def add_word_function(call):
    bot.send_message(call.from_user.id, 'Чуи, мы дома')
    show_main_menu(call)


bot.polling(none_stop=True, interval=0)
