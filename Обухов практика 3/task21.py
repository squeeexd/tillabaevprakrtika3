RUS = ["а", "е", "ё", "и", "о", "э", "ю", "я", "ы"]
ENG = {"a", "e", "i", "o", "u"}
letter = input("Введите букву: ")
if letter in RUS or letter in ENG:
    print("Буква является гласной.")
elif letter == "y" or letter == "у":
    print("Буква является согласной или гласной.")
else:
    print("Буква является согласной.")