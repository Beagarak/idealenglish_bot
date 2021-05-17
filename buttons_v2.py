import telebot
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


class LocalButtons:
    def __init__(self):
        self.name = ''
        self.create_button = telebot.types.InlineKeyboardButton(text=self.name,
                                                                callback_data=self.name)


class StatisticButton(LocalButtons):
    def __init__(self):
        super().__init__()
        self.name = 'statistic'
        self.create_button = telebot.types.InlineKeyboardButton(text=statistic,
                                                                callback_data=statistic)

    # def second_level_of_buttons(self):
    #     new_keyboard = telebot.types.InlineKeyboardMarkup()
    #     approve_button = telebot.types.InlineKeyboardButton(
    #         text=buttons.approve,
    #         callback_data=buttons.approve)
    #     reject_button = telebot.types.InlineKeyboardButton(text=buttons.reject,
    #                                                        callback_data=buttons.reject)
    #     exit_button = telebot.types.InlineKeyboardButton(
    #         text=buttons.exit_to_main_menu,
    #         callback_data=buttons.exit_to_main_menu)
    #     new_keyboard.add(approve_button, reject_button)
    #     new_keyboard.add(exit_button)
    #     bot.send_message(call.from_user.id, text='Выберите:',
    #                      reply_markup=new_keyboard)


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
    statistic_button = StatisticButton()
    # statistic_button = telebot.types.InlineKeyboardButton(text=statistic,
    #                                                       callback_data=statistic)
    translate_button = telebot.types.InlineKeyboardButton(text=translate,
                                                          callback_data=translate)
    user_markup.add(add_word_button, learn_words_button)
    user_markup.add(check_knowledge_button)
    user_markup.add(statistic_button, translate_button)
    bot.send_message(message.from_user.id, 'Выберите действие',
                     reply_markup=user_markup)
