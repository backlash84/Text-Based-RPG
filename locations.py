#!/usr/bin/env python3

from items import mushroom, machete, log, axe, stone, pickaxe, copper_ore, item_values, item_dict
from functions import invalid

class Location:
    def location(self):
        print("You are at the", self.name)
        print(self.description)
        print("Options:" + self.options)


class Forest(Location):
    def __init__(self):
        self.name = "Forest"
        self.description = "The forest is densely packed with trees and rich with foliage."
        self.options = "\n -Chop wood \n -Go to town \n -Go to clearing \n -Go to rocky hillside \n -Search \n -Inventory"

    def action(self, player):
        print(self.location())
        x = 0
        while x == 0:
            option = input("> ")
            if option.lower() == ("chop wood"):
                player.cut_tree()

            elif option.lower() == ("go to town"):
                return town

            elif option.lower() == ("go to clearing"):
                print("Place clearing function here.")

            elif option.lower() == ("go to rocky hillside"):
                return rocky_hillside

            elif option.lower() == ("search"):
                player.search(mushroom)

            elif option.lower() == ("inventory"):
                player.inventory()

            elif option.lower() == ("character sheet"):
                player.character_sheet()

            else:
                invalid()


class Town(Location):
    def __init__(self):
        self.name = "Town"
        self.description = "A quaint little town with simple wood buildings."
        self.options = "\n -Go to general store\n -Go to forest\n -Inventory"

    def action(self, player):
        print(self.location())
        x = 0
        while x == 0:
            option = input("> ")
            if option.lower() == ("go to general store"):
                return general_store
            elif option.lower() == ("go to forest"):
                return forest
            elif option.lower() == ("inventory"):
                player.inventory()
            else:
                invalid()


class GeneralStore(Location):
    def __init__(self):
        self.name = "General store"
        self.description = "A cluttered little shop filled with many different odds and ends."
        self.options = "\n -Buy\n -Sell\n -Inventory\n -Exit"

    def action(self, player):
        print(self.location())
        x = 0
        while x == 0:
            option = input("> ")

            if option.lower() == ("inventory"):
                player.inventory()

            elif option.lower() == ("buy"):
                self.buy(player)

            elif option.lower() == ("sell"):
                self.sell(player)

            elif option.lower() == ("give coin"): # SHH lol
                player.coin = player.coin + 100

            elif option.lower() == ("exit"):
                return town

            else:
                invalid()

    def buy(self, player):
        x = 0
        while x == 0:
            print("Item values are displayed after their name.")
            print("To purchase an item, simply type in its name.")
            print("")
            item_values()
            option = input("> ")
            input_lower = option.lower()

            if option.lower() == "inventory":
                player.inventory()

            elif input_lower in item_dict:
                player.buy_item(item_dict[input_lower])

            elif option.lower() == ("exit"):
                break

            else:
                invalid()

    def sell(self, player):
        x = 0
        while x == 0:
            print("To sell an item, simply type its name.")
            print("Sold items go for half their default value.")
            print("")
            option = input("> ")
            input_lower = option.lower()

            if option.lower() == ("inventory"):
                player.inventory()

            elif input_lower in item_dict:
                player.sell_item(item_dict[input_lower])

            elif option.lower() == ("exit"):
                break

            else:
                print("Invalid command, please try again.")

class RockyHillside(Location):
    def __init__(self):
        self.name = "Rocky Hillside"
        self.description = "A rocky outcropping surrounded by gravel and slabs of stone."
        self.options = "\n -Mine for stone\n -Mine for copper ore\n -Go to forest\n -Inventory"

    def action(self, player):
        print(self.location())
        x = 0
        while x == 0:
            option = input("> ")

            if option.lower() == ("mine for stone"):
                player.mine_ore(stone)

            elif option.lower() == ("mine for copper"):
                player.mine_ore(copper_ore)

            elif option.lower() == ("inventory"):
                player.inventory()

            elif option.lower() == ("go to forest"):
                return forest

            else:
                invalid()

# create singletons
forest = Forest()
general_store = GeneralStore()
town = Town()
rocky_hillside = RockyHillside()
