import telebot

from settings import TG_TOKEN
import trans_alg
import buttons
import bd
import basic_functions

## создаем экземпляр бота
bot = telebot.TeleBot(TG_TOKEN)


## Демонстрация главного меню.
#
#  После зпуска бота, функция отправляет главное меню
@bot.message_handler(commands=['start'])
def show_main_menu(message):
    buttons.main_menu(message)


## Обработка нажатия на кнопку "Добавить слова"
#
#  Функция отправляет уведомление о переходе в режим "Добавить слова".
@bot.callback_query_handler(func=lambda call: call.data == buttons.add_word)
def add_word_function(call):
    inform = 'Добавь слова в формате: Английское слово.Русский перевод'
    bot.send_message(call.from_user.id, inform)
    buttons.LocalButtons(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Учить слова"
#
#  Функция отправляет уведомление о переходе в режим "Учить слова".
#  Отправляет пользователю клавиатуру, для работы в режиме "Учить слова"
@bot.callback_query_handler(func=lambda call: call.data == buttons.learn_words)
def learn_word_function(call):
    inform = 'Давай поучим новые слова! (в разработке)'
    bot.send_message(call.from_user.id, inform)
    buttons.LocalButtonsLearning(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Проверить знания"
#
#  Функция отправляет уведомление о переходе в режим "Проверить знания".
#  Отправляет пользователю клавиатуру, для работы в режиме "Проверить знания"
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.check_knowledge)
def check_knowledge_function(call):
    inform = 'Пора проверить твои знания (в разработке)'
    bot.send_message(call.from_user.id, inform)
    buttons.LocalButtonsChecking(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Статистика"
#
#  Функция отправляет уведомление о переходе в режим "Статистика".
#  Отправляет пользователю клавиатуру, для работы в режиме "Статистика"
@bot.callback_query_handler(func=lambda call: call.data == buttons.statistic)
def statistic_function(call):
    bot.send_message(call.from_user.id, 'Вот твоя статистика: (в разработке)')
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Переводчик"
#
#  Функция отправляет уведомление о переходе в режим "Переводчик".
#  Запускает функцию Перевода в реальном времени
@bot.callback_query_handler(func=lambda call: call.data == buttons.translate)
def translator_function(call):
    inform = 'Введи слово, которое хочешь перевести:'
    bot.send_message(call.from_user.id, inform)

    ## Перевод в реальном времени
    #
    #  @param:  [in] message Строка, которую отправил пользователь для перевода.
    #  @retval: Бот отправляет в чат перевод и картинку к этому переводу
    @bot.message_handler(content_types=['text'])
    def translate_in_realtime(message):
        trans_alg.translation_function(message)

    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Выход в главное меню"
#
#  Запускает функцию Демонстрация главного меню
@bot.callback_query_handler(
    func=lambda call: call.data == buttons.exit_to_main_menu)
def back_to_main_menu_function(call):
    bot.send_message(call.from_user.id, 'Чуи, мы дома')
    show_main_menu(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')


## Обработка нажатия на кнопку "Добавить", в режиме переводчика
#
#  Отправляет пользователю клавиатуру для Выбора темы
@bot.callback_query_handler(func=lambda call: call.data == buttons.approve)
def choose_theme_menu(call):
    buttons.ThemeButtons(call).creating_keyboard(call)
    bot.answer_callback_query(callback_query_id=call.id, text='')

    @bot.callback_query_handler(func=lambda call: True)
    def themes_function(call):
        basic_functions.choose_your_theme(call)



bot.polling(none_stop=True, interval=0)
