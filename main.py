## Основной файл проекта
#
#  Реализует операции взаимодействия пользователя с ботом
#  @file main.py
#  @author Карагаев Валерий, Олейник Александр, Есаулов Лев,
#  @author Титова Екатерина, Пеева Софья

import telebot
from settings import TG_TOKEN
import trans_alg
import buttons
import help_information
import bd
import chek_of_knowledge
import errors

## Cоздаем экземпляр бота
bot = telebot.TeleBot(TG_TOKEN)
## Переменная для хранения сообщения от пользователя
message_text = 'Hello'
## Переменная для хранения сообщения от пользователя
message_id = 0
## Переменная для хранения статуса последней нажатой кнопки
#
# Принимает значение со статусом кнопки, которую нажал пользователь
button_status = ''
## Переменная для хранения последнего перевод от переводчика
translate_data = ''
## Переменная для хранения набора букв
#
#  Хранит в себе набор букв, необходимый для работы режима "Собери слово"
re_letters = ''
## Переменная для хранения набора букв
#
#  Хранит в себе набор букв, необходимый для работы режима "Собери слово"
er_letters = ''


## Демонстрация главного меню.
#
#  После нажатия пользователем команды "/start", функция отправляет главное меню
#  @param [in] message Сообщение от пользователя.
@bot.message_handler(commands=['start'])
def show_main_menu(message):
    buttons.main_menu(message)


## Демонстрация сообщения с основыми функциями бота
#
#  После нажатия пользователем команды "/help", функция отправляет сообщение с
#  информацией об основных функциях бота
#  @param [in] message Сообщение от пользователя.
@bot.message_handler(commands=['help'])
def launch_help(message):
    help_information.help(message)


## Обработка действий пользователя в боте
#
#  В зависимости от статуса, который возвращает каждая кнопка в меню пользователя,
#  вызывает функцию с необходимым действием
#  @param [in] message Сообщение от пользователя.
@bot.message_handler(content_types='text')
def get_words(message):
    help_information.help_commands(message)
    global message_text, message_id, button_status, translate_data
    message_text = message.text
    message_id = int(message.from_user.id)
    if button_status == 'add':
        buttons.LocalButtons(message).creating_keyboard(message)
    if button_status == 'trans':
        translate_data = trans_alg.translation_function(message_text,
                                                        message_id)
    if button_status == 'mix_rus_eng':
        chek_of_knowledge.rus_eng_check_answer(message_text, message_id,
                                               re_letters, message)
    if button_status == 'mix_eng_rus':
        chek_of_knowledge.eng_rus_check_answer(message_text, message_id,
                                               er_letters, message)
    if button_status == 'write_rus_eng':
        chek_of_knowledge.rus_eng_check_answer(message_text, message_id,
                                               re_letters, message)
    if button_status == 'write_eng_rus':
        chek_of_knowledge.eng_rus_check_answer(message_text, message_id,
                                               er_letters, message)


## Обработка нажатия на кнопку "Добавить слова"
#
#  Функция отправляет уведомление о переходе в режим "Добавить слова".
#  Переводит бота в режим "Добавить слова"
#
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.add_word)
def add_word_function(call):
    global button_status, message_text, message_id
    bot.answer_callback_query(callback_query_id=call.id, text='')
    inform = 'Добавь слова в формате: Английское слово.Русский перевод'
    bot.send_message(call.from_user.id, inform)
    button_status = 'add'


## Обработка нажатия на кнопку "Учить слова"
#
#  Функция отправляет уведомление о переходе в режим "Учить слова".
#  Отправляет пользователю клавиатуру, для работы в режиме "Учить слова"
#  Отправляет пользователю набор слов, которые он добавлял ранее
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.learn_words)
def learn_word_function(call):
    inform = 'Давай поучим новые слова!'
    bot.send_message(call.from_user.id, inform)
    words_to_learn = bd.words_to_learn(call.from_user.id)
    bot.send_message(call.from_user.id, words_to_learn)
    buttons.LocalButtonsLearning(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Проверить знания"
#
#  Функция отправляет уведомление о переходе в режим "Проверить знания".
#  Отправляет пользователю меню, для работы в режиме "Проверить знания"
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.check_knowledge)
def check_knowledge_function(call):
    inform = 'Пора проверить твои знания'
    bot.send_message(call.from_user.id, inform)
    buttons.LocalButtonsChecking(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Переводчик"
#
#  Функция отправляет уведомление о переходе в режим "Переводчик".
#  Запускает функцию Перевода в реальном времени
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.translate)
def translator_function(call):
    global message_text, button_status, first_in
    message_text = 'Hello'
    button_status = 'trans'
    bot.answer_callback_query(callback_query_id=call.id, text='')
    inform = 'Введи слово, которое хочешь перевести:'
    bot.send_message(call.from_user.id, inform)


## Обработка нажатия на кнопку "Выход в главное меню"
#
#  Запускает функцию Демонстрация главного меню
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.exit_to_main_menu)
def back_to_main_menu_function(call):
    bot.send_message(call.from_user.id, 'Чуи, мы дома')
    show_main_menu(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Добавить"
#
#  Добавляет слово, которе ввел пользователь, в базу данных или отвергает
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.approve)
def approve_button_func(call):
    global button_status, translate_data
    info = 'Ваше слово/предложение добавлено в словарь'
    inform = 'Введи слово, которое хочешь перевести:'
    err1 = 'Ваше слово не добавлено в словарь. Проверьте правильность ввода: "Eng.рус"'
    err2 = 'Слово уже находится в базе данных'
    if button_status == 'add':
        # Проверка
        if errors.word_order(message_text):
            # Если слова нет в бд
            if bd.count_if_exists(call.from_user.id, errors.change_word(message_text)) == 0:
                bd.add_to_db(message_text, message_id)
                bot.send_message(call.from_user.id, info)
            # Если есть
            else:
                bot.send_message(call.from_user.id, err2)
        else:
            bot.send_message(call.from_user.id, err1)
    if button_status == 'trans':
        bd.add_to_db(translate_data, message_id)
        bot.send_message(call.from_user.id, inform)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Eще Слова"
#
#  Отправляет новый набор слов в режиме "Учить слова"
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.other_words)
def other_words_button_func(call):
    words_to_learn = bd.words_to_learn(call.from_user.id)
    bot.send_message(call.from_user.id, words_to_learn)
    buttons.LocalButtonsLearning(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Викторина"
#
#  Запускает режим "Викторина"
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.quiz)
def quiz_button_func(call):
    global button_status
    button_status = 'quiz'
    buttons.GameButtons(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Собери слово"
#
#  Запускает режим "Собери слово"
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.easy_translate)
def easy_translate_button_func(call):
    global button_status
    button_status = 'easy_translate'
    buttons.GameButtons(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Англ - рус"
#
#  Запускает режим "Англ - рус" в режимах проверки знаний
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.eng_rus)
def eng_rus_button_func(call):
    global button_status, er_letters
    if button_status == 'quiz':
        button_status = 'quiz_eng_rus'
        chek_of_knowledge.eng_rus_quiz(bd.take_user_words(
            call.from_user.id),
            bd.take_other_words(), call)
    if button_status == 'easy_translate':
        button_status = 'mix_eng_rus'
        er_letters = chek_of_knowledge.eng_rus_letters(
            bd.take_user_words(call.from_user.id), call)
    if button_status == 'write_translate':
        button_status = 'write_eng_rus'
        er_letters = chek_of_knowledge.eng_write_translate(bd.take_user_words(
            call.from_user.id), call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Рус - англ"
#
#  Запускает режим "Рус - англ" в режимах проверки знаний
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: call.data == buttons.rus_eng)
def rus_eng_button_func(call):
    global button_status, re_letters
    if button_status == 'quiz':
        button_status = 'quiz_rus_eng'
        chek_of_knowledge.rus_eng_quiz(bd.take_user_words(
            call.from_user.id),
            bd.take_other_words(), call)
    if button_status == 'easy_translate':
        button_status = 'mix_rus_eng'
        re_letters = chek_of_knowledge.rus_eng_letters(
            bd.take_user_words(call.from_user.id), call)
    if button_status == 'write_translate':
        button_status = 'write_rus_eng'
        re_letters = chek_of_knowledge.rus_write_translate(bd.take_user_words(
            call.from_user.id), call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Следующее слово"
#
#  Отправляет пользователю новое слово в режимах проверки знаний
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.next_word)
def next_word_button_func(call):
    global button_status, re_letters, er_letters
    if button_status == 'quiz_eng_rus':
        chek_of_knowledge.eng_rus_quiz(bd.take_user_words(
            call.from_user.id),
            bd.take_other_words(), call)
    if button_status == 'quiz_rus_eng':
        chek_of_knowledge.rus_eng_quiz(bd.take_user_words(
            call.from_user.id),
            bd.take_other_words(), call)
    if button_status == 'mix_rus_eng':
        re_letters = chek_of_knowledge.rus_eng_letters(
            bd.take_user_words(call.from_user.id), call)
    if button_status == 'mix_eng_rus':
        er_letters = chek_of_knowledge.eng_rus_letters(
            bd.take_user_words(call.from_user.id), call)
    if button_status == 'write_eng_rus':
        er_letters = chek_of_knowledge.eng_write_translate(bd.take_user_words(
            call.from_user.id), call)
    if button_status == 'write_rus_eng':
        re_letters = chek_of_knowledge.rus_write_translate(bd.take_user_words(
            call.from_user.id), call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Сменить игру"
#
#  Возвращает пользователя в меню выбора режима проверки знаний
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.back_to_games)
def back_to_games_button_func(call):
    buttons.LocalButtonsChecking(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Напиши перевод"
#
#  Переводит бота в режим проверки знаний "Напиши перевод"
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.write_translate)
def write_translate_button_func(call):
    global button_status
    button_status = 'write_translate'
    buttons.GameButtons(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Проверка правильности ответов в режиме "Проверка знаний"
#
#  Вызывает функции проверки ответа и отправляет следующее слово
#  @param [in] call Данные с кнопки, которую нажал пользователь.
@bot.callback_query_handler(func=lambda call: True)
def checking_answer(call):
    if call.data == chek_of_knowledge.eng_user_word:
        bot.send_message(call.from_user.id, chek_of_knowledge.eng_inform1)
        buttons.InGameButtons(call).creating_keyboard(call)
    if call.data == chek_of_knowledge.eng_random_word:
        bot.send_message(call.from_user.id, chek_of_knowledge.eng_inform2)
        buttons.InGameButtons(call).creating_keyboard(call)
    if call.data == chek_of_knowledge.rus_user_word:
        bot.send_message(call.from_user.id, chek_of_knowledge.rus_inform1)
        buttons.InGameButtons(call).creating_keyboard(call)
    if call.data == chek_of_knowledge.rus_random_word:
        bot.send_message(call.from_user.id, chek_of_knowledge.rus_inform2)
        buttons.InGameButtons(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


bot.polling(none_stop=True, interval=0)
