from gpiozero import LED, Button
from time import sleep
from random import uniform

# This is an extended version of the first iteration.
# It supports multiple rounds of games.

left_name = input("Left player name is ")
right_name = input("Right player name is ")

led = LED(4)
left_button = Button(14)
right_button = Button(15)

game_active = False
round_number = 1

def start_round():
    global game_active
    # Turn on LED for random duration between 5 to 10 seconds.
    led.on()
    sleep(uniform(5, 10))
    led.off()
    game_active = True 

def pressed(button):
    global game_active, round_number
    if not game_active:
        return
    game_active = False
    winner = left_name if button.pin.number == 14 else right_name
    print(f"Round {round_number}: {winner} won the game")
    round_number += 1
    
left_button.when_pressed = pressed
right_button.when_pressed = pressed

while True:
    input(f"Press Enter to start Round {round_number}...")
    start_round()
    while game_active:
        sleep(0.01)
