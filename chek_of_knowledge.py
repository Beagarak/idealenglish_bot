import random
import buttons
from settings import TG_TOKEN
import telebot

bot = telebot.TeleBot(TG_TOKEN)
user__id = 739414278
eng_user_word = ''
eng_random_word = ''
eng_inform1 = ''
eng_inform2 = ''
rus_user_word = ''
rus_random_word = ''
rus_inform1 = ''
rus_inform2 = ''


def eng_rus_quiz(list_of_words, random_words, call):
    global eng_user_word, eng_random_word, eng_inform1, eng_inform2
    eng_user_word = list_of_words[1]
    eng_random_word = random_words[1]
    inform = 'Выберите перевод для слова: ' + list_of_words[0]
    eng_inform1 = 'Супер'
    eng_inform2 = 'Вы ошиблись, правильный перевод: ' + list_of_words[1]
    bot.send_message(call.from_user.id, inform)
    buttons.EngQuizButtons(call).creating_keyboard(call)


def rus_eng_quiz(list_of_words, random_words, call):
    global rus_user_word, rus_random_word, rus_inform1, rus_inform2
    rus_user_word = list_of_words[0]
    rus_random_word = random_words[0]
    inform = 'Выберите перевод для слова: ' + list_of_words[1]
    rus_inform1 = 'Супер'
    rus_inform2 = 'Вы ошиблись, правильный перевод: ' + list_of_words[0]
    bot.send_message(call.from_user.id, inform)
    buttons.RusQuizButtons(call).creating_keyboard(call)


def mixer(word):
    letters = list(word)
    random.shuffle(letters)
    return letters


def rus_eng_letters(list_of_words, call):
    trash = ' '.join(mixer(list_of_words[0]))
    inform = 'Соберите слово: ' + list_of_words[1] + ' из букв:' + '\n' + trash
    bot.send_message(call.from_user.id, inform)
    return list_of_words


def rus_eng_check_answer(user_ans, user_id, list_of_words, message):
    if list_of_words[0].lower() == user_ans.lower():
        bot.send_message(user_id, 'Правильно!')
    else:
        bot.send_message(user_id,
                         'Вы ошиблись, правильный перевод: ' + list_of_words[0])
    buttons.InGameButtons(message).creating_keyboard(message)


def eng_rus_letters(list_of_words, call):
    trash = ' '.join(mixer(list_of_words[1]))
    inform = 'Соберите слово: ' + list_of_words[0] + ' из букв:' + '\n' + trash
    bot.send_message(call.from_user.id, inform)
    return list_of_words


def eng_rus_check_answer(user_ans, user_id, list_of_words, message):
    if list_of_words[1].lower() == user_ans.lower():
        bot.send_message(user_id, 'Правильно!')
    else:
        bot.send_message(user_id,
                         'Вы ошиблись, правильный перевод: ' + list_of_words[1])
    buttons.InGameButtons(message).creating_keyboard(message)


def eng_write_translate(list_of_words, call):
    # Отправляем слово английском
    inform = 'Впишите верный перевод слова: ' + '\n' + list_of_words[0]
    bot.send_message(call.from_user.id, inform)
    return list_of_words


def rus_write_translate(list_of_words, call):
    # Отправляем слово английском
    inform = 'Впишите верный перевод слова: ' + '\n' + list_of_words[1]
    bot.send_message(call.from_user.id, inform)
    return list_of_words


# Вызов функции для мейна
# chek_of_knowledge.eng_write_translate(chek_of_knowledge.take_user_words(
#                                                     call.from_user.id), call)


