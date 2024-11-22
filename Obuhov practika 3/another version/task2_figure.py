from  countinuedQuestion import countinued

def inputNumberSides(statMessage: bool) -> int:
    numberSides = ""
    if statMessage:
        numberSides = int(input("Введите кол-во сторон \n"
        "и я угадаю какая это фигура [Я принимаю только циферки ^_^]: "))
    else:
        numberSides = int(input("Введите кол-во сторон фигуры: "))
    return numberSides

def evectionNameFigure(sidesValue: int):
    if sidesValue == 3: print("Похоже, что это треугольничек!")
    elif sidesValue == 4: print("Это четырехугольник...")
    elif sidesValue > 4: print("Все, фигуры больше четырех сторон - многоугольгники \n"
                               "поэтому, твоя фигура - многоугольник :)")
    elif sidesValue == 2: print("Почти треугольник :)")
    elif sidesValue == 1: print("Линия???, ладно, но это не фигура (-_-)")
    elif sidesValue >= 0: print("Мда... (-_-) на фигуру, это не похоже")

def main():
    countRepeat : int = 0
    isCountinued: bool = True

    while isCountinued:
        if countRepeat == 0:
            evectionNameFigure(inputNumberSides(True))
        else: evectionNameFigure(inputNumberSides(False))
        countRepeat += 1
        isCountinued = countinued()

    print("Выключаюсь -_- z..z..z...")


if __name__ == '__main__':
    main()