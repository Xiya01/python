def compare(number1, number2):
    if int(number1) > int(number2):
        print(number1)
        return
    if int(number2) > int(number1):
        print(number2)
        return
    if  int(number1) == int(number2):
        print("Podaj różne liczby!")
        compare(input("Podaj liczbę nr 1: "),input("Podaj liczbę nr 2: "))
        return

compare(input("Podaj liczbę nr 1: "),input("Podaj liczbę nr 2: "))