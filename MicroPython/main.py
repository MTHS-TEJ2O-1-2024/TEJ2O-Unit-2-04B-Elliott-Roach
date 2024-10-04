"""
Created by: Elliott
Created on: Sep 2024
This module is a Micro:bit MicroPython program dose: takes tempiture
"""

from microbit import *

temperature_in_celseis = int(-1)

display.clear()
sleep(1000)

while True:
    if button_a.is_pressed():
        temperature_in_celseis = temperature
        display.scroll("the temperature is:")
        display.show(temperature_in_celseis)
        display.scroll("C.")
