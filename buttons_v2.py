import telebot
from settings import TG_TOKEN
import buttons

bot = telebot.TeleBot(TG_TOKEN)


class LocalButtons:
    @bot.callback_query_handler(
        func=lambda call: call.data == buttons.translate)
    def __init__(self, call):
        self.exit_button = telebot.types.InlineKeyboardButton(
            text=exit_to_main_menu,
            callback_data=exit_to_main_menu)
        self.reject_button = telebot.types.InlineKeyboardButton(text=reject,
                                                                callback_data=reject)
        self.approve_button = telebot.types.InlineKeyboardButton(
            text=approve,
            callback_data=approve)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.bot = telebot.TeleBot(TG_TOKEN)
        self.new_keyboard.add(self.approve_button, self.reject_button)
        self.new_keyboard.add(self.exit_button)
        self.bot.send_message(call.from_user.id, text='Выберите:',
                              reply_markup=self.new_keyboard)


add_word = '|Добавить слова|'
learn_words = '|Учить слова|'
check_knowledge = '|Проверка знаний|'
statistic = '|Статистика|'
translate = '|Переводчик|'
approve = '|Добавить|'
reject = '|Отказаться|'
exit_to_main_menu = '|Выход в главное меню|'


@bot.message_handler(content_types='text')
def main_menu(message):
    user_markup = telebot.types.InlineKeyboardMarkup()
    add_word_button = telebot.types.InlineKeyboardButton(text=add_word,
                                                         callback_data=add_word)
    learn_words_button = telebot.types.InlineKeyboardButton(text=learn_words,
                                                            callback_data=learn_words)
    check_knowledge_button = telebot.types.InlineKeyboardButton(
        text=check_knowledge, callback_data=check_knowledge)
    statistic_button = telebot.types.InlineKeyboardButton(text=statistic,
                                                          callback_data=statistic)
    translate_button = telebot.types.InlineKeyboardButton(text=translate,
                                                          callback_data=translate)
    user_markup.add(add_word_button, learn_words_button)
    user_markup.add(check_knowledge_button)
    user_markup.add(statistic_button, translate_button)
    bot.send_message(message.from_user.id, 'Выберите действие',
                     reply_markup=user_markup)
