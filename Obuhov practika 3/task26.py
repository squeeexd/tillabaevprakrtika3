BANKNOTES = {
    1: "Джордж Вашингтон",
    2: "Томас Джефферсон",
    5: "Авраам Линкольн",
    10: "Александр Гамильтон",
    20: "Эндрю Джексон",
    50: "Улисс Грант",
    100: "Бенджамин Франклин"
}

nominal = input("Введи номинал банкноты: ")

if nominal.isdigit():
    nominal = int(nominal)
    if nominal in BANKNOTES:
        print(f"На банкноте в ${nominal} изображен(а) {BANKNOTES[nominal]}.")
    else:
        print("Такого номинала нет! Давай по новой!")
else:
    print("Вводи нормальное число!")