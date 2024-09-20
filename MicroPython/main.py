"""
Created by: Elliott
Created on: Sep 2024
This module is a Micro:bit MicroPython program dose: takes tempiture
"""

from microbit import *

temperature = input.temperature

display.clear

with True:
    if button_a.is_pressed():
        temperature = input.temperature()
        display.scroll("the temperature is:")
        display.show("temperature")
        display.scroll("C.")
