import telebot
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)
add_word_button = 'Добавить слова'
learn_words_button = 'Учить слова'
check_knowledge_button = 'Проверка знаний'
statistic_button = 'Статистика'
translate_button = 'Переводчик'


@bot.message_handler(commands=['start'])
def main_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row(add_word_button)
    user_markup.row(learn_words_button)
    user_markup.row(check_knowledge_button)
    user_markup.row(statistic_button, translate_button)
    bot.send_message(message.from_user.id, 'Добро пожаловать ',
                     reply_markup=user_markup)
