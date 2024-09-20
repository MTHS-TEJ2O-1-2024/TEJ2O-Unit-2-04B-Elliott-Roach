"""
Created by: Elliott
Created on: Sep 2024
This module is a Micro:bit MicroPython program dose: takes tempiture
"""

from microbit import *

temperature_ = temperature

display.clear()
sleep(1000)

with True:
    if button_a.is_pressed():
        temperature = input.temperature()
        display.scroll("the temperature is:")
        display.show(temperature_)
        display.scroll("C.")
