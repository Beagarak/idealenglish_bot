import telebot
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)
#asasasasasas

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Добавить слова')
    user_markup.row('Учить слова')
    user_markup.row('Проверка знаний')
    user_markup.row('Статистика', 'Помощь')
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)

