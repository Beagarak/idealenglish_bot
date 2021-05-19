import buttons
import telebot
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


def choose_your_theme(call):
    if call.data == buttons.no_theme:
        bot.send_message(call.from_user.id, 'Запишем в общую таблицу')
        bot.answer_callback_query(callback_query_id=call.id, text='')
    if call.data == buttons.choose_theme_adding:
        bot.send_message(call.from_user.id, 'Тут должен быть список тем')
        bot.answer_callback_query(callback_query_id=call.id, text='')
    if call.data == buttons.own_theme:
        bot.send_message(call.from_user.id, 'Пиши свою тему')
        bot.answer_callback_query(callback_query_id=call.id, text='')


