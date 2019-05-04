#!/usr/bin/env python3

import random

import items
from skills import scavenging, strength
from functions import sleep

class Player:
    def __init__(self, name, coin, energy, health, armour):
        self.name = name
        self.skills = [scavenging, strength] # set initial skills
        self.coin = coin
        self.items = items.initial_items.copy() # set initial items
        self.energy = energy
        self.health = health
        self.armour = armour
        self.timers = []
        self.location = None

    def one_turn(self):
        self.location = self.location.action(self)
        print()

    def inventory(self):
        print("Health: " + str(self.health))
        print("Energy: " + str(self.energy))
        print("Coin: " + str(self.coin))
        print("")
        print("ITEMS")
        print("")
        self.inventory_items()

    def inventory_items(self):
        for item_var in set(self.items):
            print(item_var.name + ": " + str(self.items.count(item_var)))

    def character_sheet(self):
        print("Player name: " + self.name)
        print("")
        print("Active timers:")
        for y in set(self.timers):
            print(y + " day " + str(self.timers.count(y)))
        print("")
        print("Skills:")
        for var in set(self.skills):
            print(var.name + " level " + str(self.skills.count(var)) + ": " + var.description)

    # these methods can be here or you could design them to be in the respective location classes
    def cut_tree(self):
        if self.items.count(items.axe) >= 1:
            sleep(11 - self.skills.count(strength)) # this will cause an error when the time goes negative
            self.items.append(items.log)
            self.energy = self.energy - 10
            print("You cut down a tree using your axe, and you receive one wood log!")
        elif self.items.count(items.machete) >= 1:
            sleep(11 - self.skills.count(strength))
            self.items.append(items.log)
            self.energy = self.energy - 20
            print("You cut down a tree using your machete, and you receive one wood log!")
        else:
            print("You have nothing with which to chop the wood.")

    def mine_ore(self, ore):
        if self.items.count(items.pickaxe) >= 1:
            sleep(10)
            self.items.append(ore)
            self.energy = self.energy - 10
            if ore == items.stone:
                print("You manage to break a slap of stone free from the surrounding rock.")
            else:
                print("After some effort, you manage to harvest a decent amount of " + ore.name + ".")

    def search(self, item):
        probability = ['find', 'nothing']
        result = random.choices(probability, weights=[self.skills.count(scavenging), 4], k=1)[0]
        if result == 'find':
            sleep(5)
            self.items.append(item)
            print("You found a " + item.description + "!")
        elif result == 'nothing':
            sleep(5)
            print("You found nothing of value")
        else:
            print("Error, command incorrect. BAD PROGRAMMER!")

    def buy_item(self, item):
        if self.coin >= item.value:
            self.items.append(item)
            self.coin = self.coin - item.value
            print("Bought one", item.name)
        else:
            print("You don't have enough coin!")

    def sell_item(self, item):
        if self.items.count(item) > 0:
            self.items.remove(item)
            self.coin = self.coin + item.value
            print("Sold one", item.name)
        else:
            print("You don't have any to sell!")

