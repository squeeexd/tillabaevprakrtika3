month30 = ["Апрель", "Июнь", "Сентябрь", "Ноябрь"]
month31 = ["Январь", "Март", "Май", "Июль", "Август", "Октябрь", "Декабрь"]
monthfebr = "Февраль"

month = input("Введите название месяца с Заглавной буквы: ")

if month in month30:
    print(f"{month} имеет 30 дней.")
elif month in month31:
    print(f"{month} имеет 31 день.")
elif month == monthfebr:
    print(f"{month} может состоять из 28 или 29 дней.")
else:
    print("Некорректное название месяца.")