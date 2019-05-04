#!/usr/bin/env python3

"""
A module that pretends to play for testing.
"""

test = iter([
    "start",
    "chop wood",
    "go to town",
    "go to general store",
    "buy",
    "pick axe",
    "inventory",
    "exit",
    "sell",
    "machete",
    "exit",
    "exit",
    "go to forest",
    "chop wood",
    "go to rocky hillside",
    "mine for stone",
    "mine for copper",
    ])

def fake_input(prompt=""):
    try:
        command = next(test)
        print(command)
    except StopIteration:
        command = input()
    return command

import main
main.input = fake_input
import locations
locations.input = fake_input
import functions
functions.DEBUG = True
main.main()

