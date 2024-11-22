MONTH_TEXT = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

month = int(input("Введите номер месяца (1-12): "))
day = int(input("Введите день: "))

if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day < 20):
    season = "зима"
elif (month == 3 and day >= 20) or (month <= 5) or (month == 6 and day < 21):
    season = "весна"
elif (month == 6 and day >= 21) or (month <= 8) or (month == 9 and day < 23):
    season = "лето"
else:
    season = "осень"

print(f"Введенная дата: {day} {MONTH_TEXT[month - 1]} - это {season}.")