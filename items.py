#!/usr/bin/env python3

class Item:
    def __init__(self, name, value, description):
        self.name = name
        self.value = (value)
        self.sell = (value/2)
        self.description = description

mushroom = Item("Mushroom", 3, "A forest mushroom, in good condition, commonly used in food and medicine.")
machete = Item("Machete", 5, "A long bladed machete, multi-purpose. Costs 20 energy to cut down a tree.")
log = Item("Log", 1, "A simple wooden log.")
axe = Item("Axe", 10, "A long handled axe, purpose built for cutting trees, costing only 10 energy.")
stone = Item("Stone", 1, "A simple slab of stone.")
pickaxe = Item("Pick axe", 15, "A simple mining tool used to gather stone and ore from the earth.")
copper_ore = Item("Copper ore", 2, "A mixture of raw copper and grit.")
scythe = Item("scythe", 10, "A bladed tool, usually used in farm work.")

item_list = [mushroom, machete, log, axe, stone, pickaxe, copper_ore, scythe]
item_dict = {item_var.name.lower():item_var for item_var in item_list}
initial_items = [machete, pickaxe, scythe]

def item_values():
    for item_var in item_list:
        print(item_var.name + ": " + str(item_var.value))
