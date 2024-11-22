;from enum import Enum

class vowelStatys(Enum):
    absolutely = 1
    perhaps = 2
    never = 3

RUSSIANVOWELETTERS = ('а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я')
ENGLISHVOWELLETTERS = ('a', 'e', 'i', 'o', 'u')

def inputLetter(startMessage: bool) -> str:
    currentLetter = ""
    if startMessage:
        currentLetter = input("Введите букву английского или "
                         "русского алфавита \nпрограмма выдаст, "
                         "насколько ваша буква гласная: ")[:1]
    else:
        currentLetter = input("Введите букву английского или русского алфавита: ")[:1]
    currentLetter.lower()
    return currentLetter

def vowelLetterTest(letter: str) -> vowelStatys:
    currentVowelStatys = vowelStatys
    if letter in RUSSIANVOWELETTERS:
        currentVowelStatys = vowelStatys.absolutely
    elif letter in ENGLISHVOWELLETTERS:
        currentVowelStatys = vowelStatys.absolutely
    elif letter == "y":
        currentVowelStatys = vowelStatys.perhaps
    else:
        currentVowelStatys = vowelStatys.never
    return currentVowelStatys

def messageVowelStatys(curentVowelStatus: vowelStatys, letter):
    if curentVowelStatus == vowelStatys.absolutely: print(f"Буква '{letter}' 100% гласная!")
    elif curentVowelStatus == vowelStatys.perhaps: print(f"Буква '{letter}' на 50% гласная...")
    else: print(f"В букве '{letter}' 0% гласности, соболезную :(")

def countinued() -> bool:
    toBeContinued = ""
    while toBeContinued != "y" or "n":
        toBeContinued = input("Продолжить (y/n): ")
        toBeContinued = toBeContinued.lower()
        if toBeContinued == "y": return True
        elif toBeContinued == "n": return False
        else: print("Пожалуйтса, используйте y или n ")

def main():
    countinuedValue = True
    countRepeat = 0
    while countinuedValue == True:
        if countRepeat == 0: letter = inputLetter(False)
        else: letter = inputLetter(True)
        messageVowelStatys(vowelLetterTest(letter), letter)
        countinuedValue = countinued()
        countRepeat += 1
    print("Выключаюсь -_- z..z..z...")

if __name__ == '__main__':
    main()