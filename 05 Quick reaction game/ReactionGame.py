from gpiozero import LED, Button
from time import sleep
from random import uniform
from os import _exit

left_name = input("Left player name is ")
right_name = input("Right player name is ")

def pressed(button):
    if button.pin.number == 14:
        print(left_name + " won the game")
    else:
        print(right_name + " won the game")
    _exit(0)

led = LED(4)
right_button = Button(15)
left_button = Button(14)

# Turn on LED for random duration between 5 to 10 seconds.
led.on()
sleep(uniform(5, 10))
led.off()

right_button.when_pressed = pressed
left_button.when_pressed = pressed
