import buttons
import telebot
from settings import TG_TOKEN
import bd

bot = telebot.TeleBot(TG_TOKEN)


def add_words(message):
    user_words = message.text
    user_id = message.from_user.id
    bd.add_to_db(user_words, user_id)


