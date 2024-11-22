china_animal = {
    8: "Дракон",
    9: "Змея",
    10: "Лошадь",
    11: "Коза",
    0: "Обезьяна",
    1: "Петух",
    2: "Собака",
    3: "Свинья",
    4: "Крыса",
    5: "Бык",
    6: "Тигр",
    7: "Кролик"
    }

birth_date = int(input("Введите свой год рождения:"))
if birth_date > 0:
    if birth_date % 12 == 0:
        print(f"Ваш животный знак - {china_animal[0]}")
    elif birth_date % 12 == 1:
        print(f"Ваш животный знак - {china_animal[1]}")
    elif birth_date % 12 == 2:
        print(f"Ваш животный знак - {china_animal[2]}")
    elif birth_date % 12 == 3:
        print(f"Ваш животный знак - {china_animal[3]}")
    elif birth_date % 12 == 4:
        print(f"Ваш животный знак - {china_animal[4]}")
    elif birth_date % 12 == 5:
        print(f"Ваш животный знак - {china_animal[5]}")
    elif birth_date % 12 == 6:
        print(f"Ваш животный знак - {china_animal[6]}")
    elif birth_date % 12 == 7:
        print(f"Ваш животный знак - {china_animal[7]}")
    elif birth_date % 12 == 8:
        print(f"Ваш животный знак - {china_animal[8]}")
    elif birth_date % 12 == 9:
        print(f"Ваш животный знак - {china_animal[9]}")
    elif birth_date % 12 == 10:
        print(f"Ваш животный знак - {china_animal[10]}")
    elif birth_date % 12 == 11:
        print(f"Ваш животный знак - {china_animal[11]}")
    else:
        print("Неправильный год")
else:
    print("Неправильный год")