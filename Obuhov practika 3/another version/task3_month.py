from  countinuedQuestion import countinued

class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'

MONTH = ("январь", "февраль", "март", "апрель", "май", "июнь", "июль",
        "август", "сентябрь", "октябрь", "ноябрь", "декабрь")
MONTHMINI = ("янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек")


def inputMonthName(startMessage: bool) -> str:
    if startMessage:
        print("Я помогу узнать сколько дней в месяце,\n"
        "просто напиши его название или число (1-12) (^_^) : ", end="")
    else:
        print("Напиши название или число месяца: ", end="")
    currentMonth: str = input()
    return  currentMonth

def calculateMonth(currentMonth) -> int:
    currentMonthNumber: int = 0
    if currentMonth.isdigit():
        currentMonth = int(currentMonth)
        if currentMonth > 12:
            currentMonthNumber = 11
            print("Слишком большой месяц, напоминаю, что их всего 12"
                  "\n буду считать, что вы написали 12, чтож...")
        elif currentMonth < 1:
            print("Слишком маленький... месяц, напишу, что вы выбрали первый (-_-)")
            currentMonthNumber = 0
        else:
            currentMonthNumber = (currentMonth - 1)
    elif currentMonth in MONTH:
        currentMonthNumber = MONTH.index(currentMonth)
    elif currentMonth in MONTHMINI:
        currentMonthNumber = MONTHMINI.index(currentMonth)

    return currentMonthNumber

def messageToMonth(month: int):
    MESSAGE = "В месяце"
    ENDMESSAGE = "дней (^_^)"
    if month != 1:
        # Сентябрь 30 дней. 8-ой в списке
        if month % 2 == 0:
            print(MESSAGE , str(MONTH[month]).upper() + " 30 " + ENDMESSAGE )
        elif month % 2 == 1:
            print(MESSAGE , str(MONTH[month]).upper() + " 31 " + ENDMESSAGE )
    elif month == 1:
        print(MESSAGE + str(MONTH[month]).upper() + "28 и 29 дней, это зависит от года, год может быть високосным \n"
        "https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BE%D0%B4")
    else:
        raise MyCustomError("Not correct month")

def main():
    countRepeat: int = 0
    isCountead: bool = True
    len(MONTH)
    while isCountead:
        if countRepeat == 0:
            messageToMonth(calculateMonth(inputMonthName(True)))
        else:
            messageToMonth(calculateMonth(inputMonthName(False)))
        countRepeat += 1
        isCountead = countinued()

    print("Выключаюсь -_- z..z..z...")



if __name__ == '__main__':
    main()