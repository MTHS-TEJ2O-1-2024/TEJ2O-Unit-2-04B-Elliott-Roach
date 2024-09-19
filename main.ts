/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by:Elliott
 * Created on: Sep 2024
 * This program takes temperature
*/

let temperature: number

basic.clearScreen()
basic.pause(1000)

input.onButtonPressed(Button.A, function(){
    temperature = input.temperature()
    basic.showString('the temperature is:')
    basic.showNumber(temperature )
    basic.showString('C.')
    basic.showIcon(IconNames.Happy)
})

