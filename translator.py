from translate import Translator

c = input()
type_of_lang = int(ord(c[0]))
if 1103 >= type_of_lang >= 1040:
    from_l = 'russian'
    to_l = 'english'
elif 122 >= type_of_lang >= 65:
    from_l = 'english'
    to_l = 'russian'
translator = Translator(from_lang=from_l, to_lang=to_l)
translation = translator.translate(c)

print(translation)