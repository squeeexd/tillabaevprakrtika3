NOISE_LEVELS = {
    "Тихая комната": 40,
    "Будильник": 70,
    "Газовая газонокосилка": 106,
    "Отбойный молоток": 130,
}

min_level = min(NOISE_LEVELS.values())
max_level = max(NOISE_LEVELS.values())

input_dec = int(input("Введите уровень громкости в децибелах: "))

if input_dec < min_level:
    print(f"Уровень громкости ниже минимального ({min_level} дБ).")
elif input_dec > max_level:
    print(f"Уровень громкости выше максимального ({max_level} дБ).")
elif input_dec in NOISE_LEVELS.values():
    for source, level in NOISE_LEVELS.items():
        if level == input_dec:
            print(f"Уровень громкости {input_dec} дБ соответствует: {source}.")
else:
    lower = max([level for level in NOISE_LEVELS.values() if level < input_dec], default=None)
    upper = min([level for level in NOISE_LEVELS.values() if level > input_dec], default=None)
    
    if lower is not None and upper is not None:
        print(f"Уровень громкости {input_dec} дБ находится между {lower} дБ и {upper} дБ.")
    else:
        print("Не удалось определить уровень громкости.")