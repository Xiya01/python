import os, time #chce utworzyc znikajace polecenie w terminalu

def game():
# ustalam co to za slowo, oraz numer prob
    word = input("Wpisz słowo dla przeciwnika: ")
    os.system('cls')

    start = ""
    nb_of_tries = 5
    print("Ilość liter:  " + str(len(word)) + ". Liczba prób: " + str(nb_of_tries))

    #tworzenie planszy
    for _ in word: 
        start = start + "*"
    print(start)

    while nb_of_tries > 0:
        nb_of_tries = nb_of_tries - 1
        letter = input("podaj litere: ")

        for c in start: # nie mozna wpisywac dwoch takich samych literek
            if c == letter:
                os.system('cls')
                print("Wpisz inną literę")
                break          
        i = 0
        y = "nie" 
        for x in word:
            if letter == x: #sprawdza czy wpisana litera jest rowna literce ze slowa ze zmiennej word
                y = "tak"
                start = list(start)
                start[i] = letter
                start = "".join(start) #join jak z listy chce zrobic string  
            i += 1
        
        if y == "tak": # sprawdza czy to wystepuje
            nb_of_tries = nb_of_tries + 1 
        
        print(start)

        if letter == word: #wygrana
            print("Gratulacje! To jest właściwe słowo!")
            print("") 
            print("")
            break

        if start == word: #wygrana  
            print("Gratulacje! To jest właściwe słowo!")
            print("")
            print("")
            break

        if nb_of_tries == 0: #przegrana
            print("Spróbuj jeszcze raz")
            print("")
            print("")

def player_1(): #gracz1
    print("Witaj graczu nr 1")

def player_2(): #gracz2
    print("Witaj graczu nr 2")


while True:
    i = 0
    choice = input("Witaj graczu! Wybierz jedną z opcji: \n 1. Start \n 2. Wyjście \n ")
    while i <= 2: #ilosc rund
        if choice == "1":
            time.sleep(1)
            os.system('cls')
            player_1()
            game()
            time.sleep(1)
            os.system('cls')
            player_2()
            game()
            time.sleep(1)
            os.system('cls')
        i += 1
    if choice == "2":
        break



