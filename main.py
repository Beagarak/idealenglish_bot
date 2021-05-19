import telebot

from settings import TG_TOKEN
import trans_alg
import buttons
import bd

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def show_main_menu(message):
    buttons.main_menu(message)


@bot.callback_query_handler(func=lambda call: call.data == buttons.add_word)
def add_word_function(call=buttons.add_word):
    bot.send_message(call.from_user.id,
                     'Можешь добавить свои слова! (в разработке)')
    buttons.LocalButtons(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id,
                              text='')


@bot.callback_query_handler(func=lambda call: call.data == buttons.learn_words)
def learn_word_function(call):
    bot.send_message(call.from_user.id,
                     'Давай поучим новые слова! (в разработке)')
    buttons.LocalButtonsLearning(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id,
                              text='')


@bot.callback_query_handler(
    func=lambda call: call.data == buttons.check_knowledge)
def check_knowledge_function(call):
    bot.send_message(call.from_user.id,
                     'Пора проверить твои знания (в разработке)')
    buttons.LocalButtonsChecking(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id,
                              text='')


@bot.callback_query_handler(func=lambda call: call.data == buttons.statistic)
def statistic_function(call=buttons.translate):
    bot.send_message(call.from_user.id, 'Вот твоя статистика: (в разработке)')
    bot.answer_callback_query(callback_query_id=call.id,
                              text='')


@bot.callback_query_handler(func=lambda call: call.data == buttons.translate)
def translator_function(call):
    bot.send_message(call.from_user.id,
                     'Введи слово, которое хочешь перевести:')

    @bot.message_handler(content_types=['text'])
    def translate(message):
        type_of_lang = int(ord(message.text[0]))
        log_words = trans_alg.get_translate(type_of_lang, message.text)
        translation = log_words[2]
        log_words.pop(2)
        bot.send_message(message.from_user.id, translation)
        bot.send_photo(chat_id=message.chat.id,
                       photo=trans_alg.get_picture(translation))
        buttons.LocalButtons(call).creating_keyboard(call)
        log_user_id = message.chat.id
        log_theme = "default"
        bd.add_to_db(log_words, log_theme, log_user_id)

    bot.answer_callback_query(callback_query_id=call.id,
                                  text='')


@bot.callback_query_handler(
    func=lambda call: call.data == buttons.exit_to_main_menu)
def add_word_function(call):
    bot.send_message(call.from_user.id, 'Чуи, мы дома')
    show_main_menu(call)
    bot.answer_callback_query(callback_query_id=call.id,
                              text='')


bot.polling(none_stop=True, interval=0)