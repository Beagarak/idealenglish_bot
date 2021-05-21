import telebot
from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['help'])
def help(message):
    inform = '''В главном меню выберете необходимую функцию.
                -Чтобы узнать подробнее о работе с функциями
                *Переводчик введите /translate
                *Добавить слова введите /add
                *Учить слова введите /learn
                -Узнать больше об интерактивных играх
                *Верный ли перевод? введите /guess
                *Викторина(англ-рус) введите /guess_rus
                *Викторина(рус-англ) введите /guess_eng
                *Напиши перевод введите /wr_translate
                *Собери слово введите /coword'''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['translate'])
def translate(message):
    inform = '''Отправьте в чат бота сообщение с необходимым
                для перевода словом/предложением.
                Бот выдаст перевод и картинку.'''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['add'])
def add(message):
    inform = '''В чат бота отправьте сообщение 'слово'.'перевод слова'и укажите
     тему слова.Слово будет добавлено в словарь бота.'''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['stat'])
def stat(message):
    inform = '''Бот выведет статистику выученных пользователем слов.'''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['learn'])
def learn(message):
    inform = '''Выберете тему слов, планируемых для изучения, и их
    количество. Бот выдаст сообщение в формате связки cлово-перевод. '''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['guess'])
def guess(message):
    inform = '''У вас появится связка 'слово-перевод' и 2 кнопки: Верно и
    Неверно. Необходимо отметить, верно ли указан перевод. '''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['guess_rus'])
def guess_rus(message):
    inform = '''Бот выдаст слово на английском языке и 3 варианта
    перевода на русский, необходимо выбрать верный вариант перевода
    слова. '''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['guess_eng'])
def guess_eng(message):
    inform = '''Бот выдаст слово на русском языке и 3 варианта перевода
    на английский, необходимо выбрать верный вариант перевода слова. '''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['wr_translate'])
def wr_translate(message):
    inform = '''Бот выдаст слово на английском языке, необходимо
    отправить в чат бота сообщение с переводом данного слова на русский. '''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(commands=['coword'])
def coword(message):
    inform = '''Бот выдаст слово на русском языке, необходимо из набора
    английских букв собрать слово-перевод. '''
    bot.send_message(message.from_user.id, inform)


@bot.message_handler(content_types='text')
def help_commands(message):
    command = message.text
    if command == '/help':
        help(message)
    if command == '/translate':
        translate(message)
    if command == '/add':
        add(message)
    if command == '/learn':
        learn(message)
    if command == '/guess':
        guess(message)
    if command == '/guess_rus':
        guess_rus((message))
    if command == '/guess_eng ':
        guess_eng(message)
    if command == '/wr_translate':
        wr_translate(message)
    if command == '/coword':
        coword(message)