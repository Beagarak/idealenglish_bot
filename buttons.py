## Конструктор всех кнопок для бота
#
# Задаёт разметку и расположение всех меню-кнопок для бота
# @file buttons.py
# @author Олейник Александр
import telebot
from settings import TG_TOKEN
import chek_of_knowledge

## Создаём экземпляр бота
bot = telebot.TeleBot(TG_TOKEN)


## Класс, отвечающий за создание клавиатуры для режима "Переводчик"
#
# Создаёт кнопки "Добавить" и "Выход в главное меню"
class TranslateButtons:
    ## Конструктор класса
    # @param user_id: id пользователя из Telegram
    def __init__(self, user_id):
        self.approve_b = telebot.types.InlineKeyboardButton(
            text=approve,
            callback_data=approve)
        self.exit_b = telebot.types.InlineKeyboardButton(
            text=exit_to_main_menu,
            callback_data=exit_to_main_menu)
        self.bot = telebot.TeleBot(TG_TOKEN)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.approve_b)
        self.new_keyboard.add(self.exit_b)

    ## Метод, отправляющий клавиатуру с сообщением "Выберите"
    #
    # Клавиатура отправляется после получения id пользователя
    # @param self: Описание объекта
    # @param user_id: id пользователя из Telegram
    def creating_translate_keyboard(self, user_id):
        self.bot.send_message(user_id, text='Выберите',
                              reply_markup=self.new_keyboard)


## Основной класс, отвечающий за создание базовых кнопок и любых клавиатур
#
# Создаёт кнопки "Добавить", "Выход в главное меню" и "Сменить игру"
# Конкретно этот класс создаёт клавиатуру для режима "Добавить слова"
class LocalButtons:
    ## Конструктор класса
    # @param call: Данные с кнопки
    def __init__(self, call):
        self.approve_b = telebot.types.InlineKeyboardButton(
            text=approve,
            callback_data=approve)
        self.exit_b = telebot.types.InlineKeyboardButton(
            text=exit_to_main_menu,
            callback_data=exit_to_main_menu)
        self.back_to_games_b = telebot.types.InlineKeyboardButton(
            text=back_to_games,
            callback_data=back_to_games)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.bot = telebot.TeleBot(TG_TOKEN)
        self.new_keyboard.add(self.approve_b)
        self.new_keyboard.add(self.exit_b)

    ## Метод, отправляющий клавиатуру с сообщением "Выберите"
    #
    # Клавиатура отправляется после получения данных с кнопки
    # @param self: Описание объекта
    # @param call: Данные с кнопки
    def creating_keyboard(self, call):
        self.bot.send_message(call.from_user.id, text='Выберите',
                              reply_markup=self.new_keyboard)


## Наследуемый от основного класс, отвечающий за создание кнопок к режиму "Учить слова"
#
# Создаёт кнопку "Ещё слова"
class LocalButtonsLearning(LocalButtons):
    ## Конструктор класса
    def __init__(self, call):
        super().__init__(call)
        self.other_words_b = telebot.types.InlineKeyboardButton(
            text=other_words,
            callback_data=other_words)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.other_words_b)
        self.new_keyboard.add(self.exit_b)


## Наследуемый от основного класс, отвечающий за создание кнопок к режиму "Проверка знаний"
#
# Создаёт кнопки "Викторина", "Напиши перевод" и "Собери слово"
class LocalButtonsChecking(LocalButtons):
    ## Конструктор класса
    def __init__(self, call):
        super().__init__(call)
        self.quiz_button = telebot.types.InlineKeyboardButton(
            text=quiz,
            callback_data=quiz)
        self.write_translate_button = telebot.types.InlineKeyboardButton(
            text=write_translate,
            callback_data=write_translate)
        self.easy_translate_button = telebot.types.InlineKeyboardButton(
            text=easy_translate,
            callback_data=easy_translate)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.quiz_button)
        self.new_keyboard.add(self.write_translate_button,
                              self.easy_translate_button)
        self.new_keyboard.add(self.exit_b)


## Наследуемый от основного класс, отвечающий за создание кнопок к игровым режимам
#
# Создаёт кнопки "Англ - рус" и "Рус - англ"
class GameButtons(LocalButtons):
    ## Конструктор класса
    def __init__(self, call):
        super().__init__(call)
        self.eng_rus_b = telebot.types.InlineKeyboardButton(
            text=eng_rus,
            callback_data=eng_rus)
        self.rus_eng_b = telebot.types.InlineKeyboardButton(
            text=rus_eng,
            callback_data=rus_eng)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.eng_rus_b, self.rus_eng_b)


## Наследуемый от основного класс, отвечающий за создание кнопок к английско-русской версии игры "Викторина"
#
# Создаёт кнопки, названия которых соответствуют названиям вариантов ответа
class EngQuizButtons(LocalButtons):
    ## Конструктор класса
    def __init__(self, call):
        super().__init__(call)
        self.answer1_b = telebot.types.InlineKeyboardButton(
            text=chek_of_knowledge.eng_user_word,
            callback_data=chek_of_knowledge.eng_user_word)
        self.answer2_b = telebot.types.InlineKeyboardButton(
            text=chek_of_knowledge.eng_random_word,
            callback_data=chek_of_knowledge.eng_random_word)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.answer1_b, self.answer2_b)


## Наследуемый от основного класс, отвечающий за создание кнопок к русско-английской версии игры "Викторина"
#
# Создаёт кнопки, названия которых соответствуют названиям вариантов ответа
class RusQuizButtons(LocalButtons):
    ## Конструктор класса
    def __init__(self, call):
        super().__init__(call)
        self.answer1_b = telebot.types.InlineKeyboardButton(
            text=chek_of_knowledge.rus_random_word,
            callback_data=chek_of_knowledge.rus_random_word)
        self.answer2_b = telebot.types.InlineKeyboardButton(
            text=chek_of_knowledge.rus_user_word,
            callback_data=chek_of_knowledge.rus_user_word)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.answer1_b, self.answer2_b)


## Наследуемый от основного класс, отвечающий за создание внутриигровых кнопок
#
# Создаёт кнопку "Следующее слово"
class InGameButtons(LocalButtons):
    ## Конструктор класса
    def __init__(self, call):
        super().__init__(call)
        self.next_word_b = telebot.types.InlineKeyboardButton(
            text=next_word,
            callback_data=next_word)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.next_word_b)
        self.new_keyboard.add(self.back_to_games_b)


## Переменные, хранящие в себе название кнопок
add_word = 'Добавить слова'
learn_words = 'Учить слова'
check_knowledge = 'Проверка знаний'
translate = 'Переводчик'
approve = 'Добавить'
exit_to_main_menu = 'Выход в главное меню'
quiz = 'Викторина'
eng_rus = 'Англ - рус'
rus_eng = 'Рус - англ'
write_translate = 'Напиши перевод'
easy_translate = 'Собери слово'
next_word = 'Следующее слово'
back_to_games = 'Сменить игру'
other_words = 'Ещё слова'


## Создание клавиатуры для главного меню
#
# Создаёт кнопки "Добавить слова", "Учить слова", "Проверка знаний" и "Переводчик"
# @param message: Сообщение от пользователя
@bot.message_handler(content_types='text')
def main_menu(message):
    user_markup = telebot.types.InlineKeyboardMarkup()
    add_word_b = telebot.types.InlineKeyboardButton(text=add_word,
                                                    callback_data=add_word)
    learn_words_b = telebot.types.InlineKeyboardButton(
        text=learn_words, callback_data=learn_words)
    check_knowledge_b = telebot.types.InlineKeyboardButton(
        text=check_knowledge, callback_data=check_knowledge)
    translate_b = telebot.types.InlineKeyboardButton(text=translate,
                                                     callback_data=translate)
    user_markup.add(add_word_b, learn_words_b)
    user_markup.add(check_knowledge_b)
    user_markup.add(translate_b)
    bot.send_message(message.from_user.id, 'Выберите действие',
                     reply_markup=user_markup)
