#!/usr/bin/env python3

"""
A module of general purpose functions that didn't really have a place anywhere else.
"""

import time
from itertools import cycle

DEBUG = False

def invalid():
    print("Invalid command, please try again.")

spinner = cycle("\|/-")
def sleep(seconds):
    for i in range(seconds*4):
        print(" Working ... ", next(spinner), end='\r', flush=True)
        time.sleep(.02 if DEBUG else .25)
