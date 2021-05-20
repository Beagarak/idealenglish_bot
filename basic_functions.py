import buttons
import telebot
from settings import TG_TOKEN
import bd

bot = telebot.TeleBot(TG_TOKEN)


def choose_your_theme(call):
    if call.data == buttons.no_theme:
        bot.send_message(call.from_user.id, 'Запишем в общую таблицу')
        bot.answer_callback_query(callback_query_id=call.id, text='')
        theme = 'Без Темы'
    if call.data == buttons.choose_theme_adding:
        bot.send_message(call.from_user.id, 'Тут должен быть список тем')
        bot.answer_callback_query(callback_query_id=call.id, text='')
        theme = 'Здесь должна быть тема, из существующих'
        ###
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
