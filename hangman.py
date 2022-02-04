import os, time


def game():
    nb_of_tries = 3
    word = input("Write your word: ")
    list1= []
    list2 =[]

    for letters in word: #put letters into a list
        list1.append(letters)
        os.system('cls')

    for a in list1: #display letter as "_" for players
        a = "_" 
        list2.append(a)        
    
    print(list2) #display list

    while nb_of_tries > 0: #game mechanics
        nb_of_tries -= 1
        letter = input("Write your letter: ")
        os.system('cls')
        for z in list2:
            if letter == z:               
                os.system('cls')
                print("Write another letter")
                break                          
        i = 0
        y = "no" 
        for x in list1: #put a correct letter to a list 
            if letter == x:
                y = "yes"
                list2[i] = letter
            i += 1
        if y == "yes":
            nb_of_tries += 1
        
        print(list2)

        if list(letter) == list1: #win condition
            os.system('cls')
            print(list1)
            print("You won!")
            break

        if nb_of_tries == 0: #lose
            print("You lost. Try again!") 
            break

        if list1 == list2: #win condition
            print("You won!")
            break

def player_1():
    print("Hello player # 1")

def player_2():
    print("Hello player # 2")

while True:
    i = 0
    player_choice = input("Hello! Choose one of the options:\n 1. Start \n 2. Exit \n" )
    while i <= 2: #number of rounds
        if player_choice == "1":
            time.sleep(1)
            os.system('cls')
            player_1()
            game()
            time.sleep(1)
            os.system('cls')
            player_2()
            game()
            time.sleep(1)
        i += 1    
    if player_choice == "2":
        break