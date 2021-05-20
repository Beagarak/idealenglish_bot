# import buttons
import telebot
from settings import TG_TOKEN
import bd

bot = telebot.TeleBot(TG_TOKEN)


def add_words(call):
    user_words = call.text
    user_id = call.from_user.id
    # bd.add_to_db(user_words, user_id)
