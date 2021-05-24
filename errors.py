def word_order(text):
    # в идеале проверить все буквы до и после точки(препинание)
    place = text.find(".")
    if place == -1:
        return 0
    elif not (65 <= int(ord(text[place - 1])) <= 122 and
              (1040 <= int(ord(text[place + 1])) <= 1103 or text[place + 1] == ' ')):
        return 0
    else:
        return 1
