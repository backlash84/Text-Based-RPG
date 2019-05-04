#!/usr/bin/env python3

from player import Player
from locations import forest
from functions import invalid

def start_menu():
    return
    os.system("cls")
    print('''Welcome to my game!
    1: start
    2: help
    3: quit   ''')

    x = 0
    while x == 0:
        option = input("> ")
        if option.lower() == ("start"):
            break
        elif option.lower() == ("help"):
            print("Help section goes here.")
        elif option.lower() == ("quit"):
            sys.exit()
        else:
            invalid()

def main():
    #### CHARACTERS ####
    main_character = Player("Adventurer", 100, 100, 100, 0)
    start_menu()
    main_character.location = forest # set initial location

    while main_character.health > 0:
        if main_character.energy <= 0:
            print("You collapse due to lack of energy, you lose 10 health.")
            main_character = main_character.health - 10
            main_character.energy = 50
        main_character.one_turn()


    print("        GAME OVER        ")
    print("Your health reached zero.")
    time.sleep(5)

while True:
    main()
