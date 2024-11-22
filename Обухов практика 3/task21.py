LETTERS = ["а", "е", "ё", "и", "о", "э", "ю", "я", "ы", "a", "e", "i", "o", "u"]
letter = input("Введите букву: ")

if letter == "y":
    print("гласная-согласная, тут не понятно")
else:
    if letter in LETTERS:
        print("буква согласная")
    else:
        print("буква гласная")