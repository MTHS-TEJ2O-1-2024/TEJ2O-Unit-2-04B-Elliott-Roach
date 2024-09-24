"""
Created by: Elliott
Created on: Sep 2024
This module is a Micro:bit MicroPython program dose: takes tempiture
"""

from microbit import *

temp_C = 0

display.clear()
sleep(1000)

while True:
    if button_a.is_pressed():
        temp_C = float(temp_C + temperature)
        display.scroll("the temperature is:")
        display.show(temp_C)
        display.scroll("C.")
