MONTH30 = ["апрель", "июнь", "сентябрь", "ноябрь"]
MONTH31 = ["январь", "март", "май", "июль", "август", "октябрь", "декабрь"]
MONTH_FEBR = "февраль"

input_month = input("Введите название месяца: ")
input_month = input_month.lower()

if input_month in MONTH30:
    print(f"{input_month} имеет 30 дней.")
elif input_month in MONTH31:
    print(f"{input_month} имеет 31 день.")
elif input_month == MONTH_FEBR:
    print(f"{input_month} может состоять из 28 или 29 дней.")
else:
    print("Некорректное название месяца.")