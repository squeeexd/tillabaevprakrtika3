from countinuedQuestion import countinued
DECIBELSLEVEL = {40 : "тихая комната", 70 : "будильник" , 106: "газовая газонокосилка", 130 : "отбойный молоток" }

def inputWhileWhenCorrect(message2input: str) -> int:

    repeatPlease = "попробуйте еще раз"
    correct = False

    while not correct:

        print(message2input, end="")
        currentInput = input()[:3]

        if currentInput.isdigit():
            currentInput = int(currentInput)
            if currentInput < 1:
                print(f"Сликом маленькое значение, {repeatPlease}")
            elif currentInput > 150:
                print(f"Кажется вы переборщили, {repeatPlease}")
            else:
                currentInput = float(currentInput)
                correct = True
        elif currentInput.isalpha():
            print(f"Сюда нужно писать циферки! {repeatPlease}")
        else:
            print(f"Я не понял, что вы написали (-_-), но сюда нужно писать циферки")
    return currentInput

def inputDecibelLevel(startMessage: bool) -> int:
    message2input: str = "введите децибелы: "

    if startMessage:
        print("Стартовый опрос ", end="")
    else:
        print("Опрос в цикле ", end="")

    currentDecibels = inputWhileWhenCorrect(message2input)
    return currentDecibels

def messenge2DecibelLevel(decibelLevel: int):
    #if decibelLevel in DECIBELSLEVEL:
     #   a = 0
    if decibelLevel < 20:
        print(f"Очень тихо, вы можете сойти сума!")
    elif decibelLevel < 40:
        print(f"Достаточно тихо, тише чем обычно")
    elif decibelLevel < 70:
        print(f"Ваша сила звука {decibelLevel.__int__()}дБ между {DECIBELSLEVEL.get(70)} и {DECIBELSLEVEL.get(40)}")
    elif decibelLevel < 106:
        print(f"Ваша сила звука {decibelLevel.__int__()}дБ между {DECIBELSLEVEL.get(106)} и {DECIBELSLEVEL.get(70)}")
    elif decibelLevel < 130:
        print(f"Ваша сила звука {decibelLevel.__int__()}дБ между {DECIBELSLEVEL.get(130)} и {DECIBELSLEVEL.get(106)}")
    else:
        print(f"Очень громко! {decibelLevel.__int__()}дБ больше чем {DECIBELSLEVEL.get(130)}")

def main():
    countRepeat: int = 0
    isCountead = True

    while isCountead:
        val = inputDecibelLevel(True)
        messenge2DecibelLevel(val)
        countRepeat += 1
        isCountead = countinued()
    print("Выключаюсь -_- z..z..z...")

if __name__ == '__main__':
    main()