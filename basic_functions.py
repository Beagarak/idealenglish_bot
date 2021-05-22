import buttons
import telebot
from settings import TG_TOKEN

# import bd


bot = telebot.TeleBot(TG_TOKEN)


def add_words(user_words, user_id):
    # bd.add_to_db(user_words, user_id)
    print(user_words,user_id)



