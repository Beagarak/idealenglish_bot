from translate import Translator


def get_translate(asci, text):
    trans_and_lang = []
    trans_and_lang.clear()
    translation = ''
    if 1103 >= asci >= 1040:
        translator = Translator(from_lang='Russian', to_lang='English')
        translation = translator.translate(text)
        trans_and_lang.append(translation)
        trans_and_lang.append(text)
        translation = translation.split('&')[0]  # отсекаем мусор, который иногда появляется
    elif 122 >= asci >= 65:
        translator = Translator(from_lang='English', to_lang='Russian')
        translation = translator.translate(text)
        trans_and_lang.append(text)
        trans_and_lang.append(translation)
    trans_and_lang.append(translation)
    return trans_and_lang


def get_picture(text):
    link = 'https://yandex.ru/images/search?text=' + text.lower() + '%20'
    return link
