# Таблица уровней громкости в децибелах
noise_levels = {
    "Тихая комната": 40,
    "Будильник": 70,
    "Газовая газонокосилка": 106,
    "Отбойный молоток": 130,
}

# Минимальный и максимальный уровни
min_level = min(noise_levels.values())
max_level = max(noise_levels.values())

# Ввод уровня громкости
dec = int(input("Введите уровень громкости в децибелах: "))

# Проверка уровня громкости
if dec < min_level:
    print(f"Уровень громкости ниже минимального ({min_level} дБ).")
elif dec > max_level:
    print(f"Уровень громкости выше максимального ({max_level} дБ).")
elif dec in noise_levels.values():
    for source, level in noise_levels.items():
        if level == dec:
            print(f"Уровень громкости {dec} дБ соответствует: {source}.")
else:
    # Находим, между какими уровнями находится введенное значение
    lower = max([level for level in noise_levels.values() if level < dec], default=None)
    upper = min([level for level in noise_levels.values() if level > dec], default=None)
    
    if lower is not None and upper is not None:
        print(f"Уровень громкости {dec} дБ находится между {lower} дБ и {upper} дБ.")
    else:
        print("Не удалось определить уровень громкости.")