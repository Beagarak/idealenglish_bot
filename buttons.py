import telebot
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


class LocalButtons:
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

    def creating_keyboard(self, call):
        self.bot.send_message(call.from_user.id, text='Выберите:',
                              reply_markup=self.new_keyboard)


class LocalButtonsLearning(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.next_word_button = telebot.types.InlineKeyboardButton(
            text=next_word,
            callback_data=next_word)
        self.choose_theme_button = telebot.types.InlineKeyboardButton(
            text=choose_theme_learning,
            callback_data=choose_theme_learning)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.next_word_button, self.choose_theme_button)
        self.new_keyboard.add(self.exit_button)


class LocalButtonsChecking(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.guess_translate_button = telebot.types.InlineKeyboardButton(
            text=guess_translate,
            callback_data=guess_translate)
        self.eng_rus_button = telebot.types.InlineKeyboardButton(
            text=eng_rus,
            callback_data=eng_rus)
        self.rus_eng_button = telebot.types.InlineKeyboardButton(
            text=rus_eng,
            callback_data=rus_eng)
        self.write_translate_button = telebot.types.InlineKeyboardButton(
            text=write_translate,
            callback_data=write_translate)
        self.easy_translate_button = telebot.types.InlineKeyboardButton(
            text=easy_translate,
            callback_data=easy_translate)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.guess_translate_button)
        self.new_keyboard.add(self.eng_rus_button, self.rus_eng_button)
        self.new_keyboard.add(self.write_translate_button,
                              self.easy_translate_button)
        self.new_keyboard.add(self.exit_button)


class ThemeButtons(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.no_theme_button = telebot.types.InlineKeyboardButton(
            text=no_theme,
            callback_data=no_theme)
        self.choose_theme_adding_button = telebot.types.InlineKeyboardButton(
            text=choose_theme_adding,
            callback_data=choose_theme_adding)
        self.own_theme_button = telebot.types.InlineKeyboardButton(
            text=own_theme,
            callback_data=own_theme)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.bot = telebot.TeleBot(TG_TOKEN)
        self.new_keyboard.add(self.no_theme_button)
        self.new_keyboard.add(self.choose_theme_adding_button)
        self.new_keyboard.add(self.own_theme_button)


add_word = '|Добавить слова|'
learn_words = '|Учить слова|'
check_knowledge = '|Проверка знаний|'
statistic = '|Статистика|'
translate = '|Переводчик|'
approve = '|Добавить|'
reject = '|Отказаться|'
exit_to_main_menu = '|Выход в главное меню|'
next_word = '|Следующее слово|'
choose_theme_learning = '|Выбери тему|'
guess_translate = '|Верный ли перевод?|'
eng_rus = '|Викторина(англ-рус)|'
rus_eng = '|Викторина(рус-англ)|'
write_translate = '|Напиши перевод|'
easy_translate = '|Угадай перевод по буквам|'
no_theme = '|Без темы|'
choose_theme_adding = '|Выбрать тему|'
own_theme = '|Новая тема|'


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


# def creating_theme_buttons(theme_value, theme_item, call):
#     theme_keyboard = telebot.types.InlineKeyboardMarkup()
#     theme_button = telebot.types.InlineKeyboardButton(text=theme_item,
#                                                       callback_data=theme_value)
#     bot = telebot.TeleBot(TG_TOKEN)
#     theme_keyboard.add(theme_button)
#     bot.send_message(call.from_user.id, '', reply_markup=theme_keyboard)
