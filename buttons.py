import telebot
from settings import TG_TOKEN
import chek_of_knowledge

##Создаём экземпляр бота
bot = telebot.TeleBot(TG_TOKEN)


##Создание базовой клавиатуры с кнопками "Добавить", "Отказаться" и "Выход в главное меню"
#
# Функция является методом основного класса и создаёт любую клавиатуру, в данном случае базовую клавиатуру с вышеуказанными кнопками
class LocalButtons:
    def __init__(self, call):
        self.exit_b = telebot.types.InlineKeyboardButton(
            text=exit_to_main_menu,
            callback_data=exit_to_main_menu)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.bot = telebot.TeleBot(TG_TOKEN)
        self.new_keyboard.add(self.exit_b)

    def creating_keyboard(self, call):
        self.bot.send_message(call.from_user.id, text='Выберите',
                              reply_markup=self.new_keyboard)


##Создание клавиатуры для режима "Переводчик"
#
# В класс, наследуемый от основного, добавляются кнопки "Добавить" и "Отказаться"
class LocalButtonsTranslate(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.approve_b = telebot.types.InlineKeyboardButton(
            text=approve,
            callback_data=approve)
        self.reject_b = telebot.types.InlineKeyboardButton(
            text=reject,
            callback_data=reject)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.approve_b, self.reject_b)
        self.new_keyboard.add(self.exit_b)


##Создание клавиатуры для режима "Учить слова"
#
# В класс, наследуемый от основного, добавляется новая кнопка "Следующее слово"
class LocalButtonsLearning(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.next_word_button = telebot.types.InlineKeyboardButton(
            text=next_word,
            callback_data=next_word)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.next_word_button)
        self.new_keyboard.add(self.exit_b)


##Создание клавитауры для функции "Проверка знаний"
#
# В класс, наследуемый от основного, добавляются новые кнопки с названиями режимов данной функции
class LocalButtonsChecking(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.guess_translate_button = telebot.types.InlineKeyboardButton(
            text=guess_translate,
            callback_data=guess_translate)
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
        self.new_keyboard.add(self.guess_translate_button)
        self.new_keyboard.add(self.quiz_button)
        self.new_keyboard.add(self.write_translate_button,
                              self.easy_translate_button)
        self.new_keyboard.add(self.exit_b)


class QuizGameButtons(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.english_russian_b = telebot.types.InlineKeyboardButton(
            text=eng_rus,
            callback_data=eng_rus)
        self.russian_english_b = telebot.types.InlineKeyboardButton(
            text=rus_eng,
            callback_data=rus_eng)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.english_russian_b, self.russian_english_b)


class EngQuizButtons(LocalButtons):
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


class RusQuizButtons(LocalButtons):
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


class LettersGameButtons(LocalButtons):
    def __init__(self, call):
        super().__init__(call)
        self.letters_eng_rus_b = telebot.types.InlineKeyboardButton(
            text=letters_eng_rus,
            callback_data=letters_eng_rus)
        self.letters_rus_eng_b = telebot.types.InlineKeyboardButton(
            text=letters_rus_eng,
            callback_data=letters_rus_eng)
        self.new_keyboard = telebot.types.InlineKeyboardMarkup()
        self.new_keyboard.add(self.letters_rus_eng_b, self.letters_eng_rus_b)


##Создаём названия и надписи для всех кнопок
add_word = '|Добавить слова|'
learn_words = '|Учить слова|'
check_knowledge = '|Проверка знаний|'
translate = '|Переводчик|'
approve = '|Добавить|'
reject = '|Отказаться|'
exit_to_main_menu = '|Выход в главное меню|'
next_word = '|Следующее слово|'
guess_translate = '|Верный ли перевод?|'
quiz = '|Викторина|'
eng_rus = '|Англ - рус|'
rus_eng = '|Рус - англ|'
write_translate = '|Напиши перевод|'
easy_translate = '|Угадай перевод по буквам|'
letters_eng_rus = '|Англ-рус|'
letters_rus_eng = '|Рус-англ|'


##Создание и вывод клавиатуры для главного меню
#
# Функция отправляет уведомление "Выберите действие"
# Функция создаёт и отпраляет пользователю клавиатуру
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
