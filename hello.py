from os import system
system("cls")
system("shutdown -s -t 3600")
def triangle():
    print("*")
    print("*  *")
    print("*    *")
    print("*******")
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
        return   
    
    if choice == "2":
        square()
        return

    if choice == "3":
        nazwa1 = int(input("Podaj liczbę nr 1: "))
        nazwa2 = int(input("Podaj liczbę nr 2: "))
        print(sum(nazwa1,nazwa2))
        return

    if choice == "4":
        number1 = int(input("Podaj liczbę nr 1: "))
        number2 = int(input("Podaj liczbę nr 2: "))
        print(diff(number1,number2))
        return

print("1. Narysowanie trójkąta.")
print("2. Narysowanie kwadratu.")
print("3. Dodawanie.")
print("4. Odejmowanie.")

number = input("Podaj numer: ")
while number != "1" and number != "2" and number != "3" and number != "4":
    number = input("Podaj numer: ")

menu(number)