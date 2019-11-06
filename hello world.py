def triangle():
    print("*")
    print("*  *")
    print("*    *")
    print("******")
    return

def square():
    print(" ______")
    print("|      |")
    print("|      |")
    print("|______|")
    return

def sum(xd,haha):
    return xd + haha

def diff(par1,par2):
    return par1 - par2

def menu(choice):
    if choice == "1":
        triangle()
        
    elif choice == "2":
        square()

    elif choice == "3":
        nazwa1 = int(input("Podaj liczbę nr 1: "))
        nazwa2 = int(input("Podaj liczbę nr 2: "))
        print(sum(nazwa1,nazwa2))

    elif choice == "4":
        number1 = int(input("Podaj liczbę nr 1: "))
        number2 = int(input("Podaj liczbę nr 2: "))
        print(diff(number1,number2))

    else:
        print("Spróbuj jeszcze raz.")


print("1. Narysowanie trójkąta.")
print("2. Narysowanie kwadratu.")
print("3. Dodawanie.")
print("4. Odejmowanie.")
number = input("Podaj numer: ")
menu(number)