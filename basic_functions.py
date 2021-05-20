import buttons
import telebot
from settings import TG_TOKEN
import bd

bot = telebot.TeleBot(TG_TOKEN)

theme = 'Без темы'


def get_themes_list(call):
    themes = bd.themes_db(call.from_user.id)
    for i, item in enumerate(themes):
        theme_name = str(i) + ' ' + item
        bot.send_message(call.from_user.id, theme_name)



def choose_your_theme(call):
    global theme
    if call.data == buttons.no_theme:
        bot.send_message(call.from_user.id, 'Запишем в общую таблицу')
        bot.answer_callback_query(callback_query_id=call.id, text='')
        theme = 'Без Темы'
    if call.data == buttons.choose_theme_adding:
        bot.send_message(call.from_user.id, 'Тут должен быть список тем')
        bot.answer_callback_query(callback_query_id=call.id, text='')
        get_themes_list(call)

        # @bot.message_handler(content_types='text')
        # def get_theme_number(message):
        #     number_of_theme = int(message.text)
        #     theme = bd.themes_db(message.from_user.id)[number_of_theme]
        #

    if call.data == buttons.own_theme:
        bot.send_message(call.from_user.id, 'Пиши свою тему')
        bot.answer_callback_query(callback_query_id=call.id, text='')
        theme = call.text
    return theme


def add_words(call):
    user_words = call.text
    user_id = call.from_user.id
    theme = choose_your_theme(call)
    bd.add_to_db(user_words, theme, user_id)
