from gpiozero import LED, Buzzer, Button
from time import sleep

# This is an adaptive version of the original Scratch project with some changes.
# Note that in this project, the lights are meant for car traffic.
# By default, green light lasts for 10 seconds, buzzer beeps slowly.
# Then, yellow light lasts for 2 seconds, buzzer beeps slowly.
# Finally, red light lasts for 5 seconds, buzzer beeps quickly. (This is time to cross.)
# If button is pressed during green light, the buzzer long-beeps once, yellow light turns on immediately.
# If button is pressed during yellow / red light, nothing happens.

red = LED(25)
yellow = LED(8)
green = LED(7)
buzzer = Buzzer(14)
button = Button(2)

# Time units all in seconds.
short_beep = 0.1
long_beep = 0.9
green_light_duration = 10
yellow_light_duration = 2
red_light_duration = 5

crossing_requested = False
phase = "green" # "green", "yellow", or "red"

def handle_crossing_request():
    global crossing_requested
    if phase == "green" and not crossing_requested:
        crossing_requested = True
        buzzer.beep(on_time = long_beep, off_time = 0, n = 1, background = True)
        # Wait for the single beep to finish.
        sleep(long_beep)
        # Then resume the slow beep for the remaining time before crossing.
        buzzer.beep(on_time = short_beep, off_time = long_beep, background = True)

button.when_pressed = handle_crossing_request

try:
    while True:
        # Green phase.
        # If pedestrian requests crossing, green will only continue for 2 more seconds.
        phase = "green"
        red.off()
        yellow.off()
        green.on()
        buzzer.beep(on_time = short_beep, off_time = long_beep, background = True)
        for _ in range(green_light_duration):
            sleep(1)
            if crossing_requested:
                break
        
        # Yellow phase.
        phase = "yellow"
        green.off()
        yellow.on()
        sleep(yellow_light_duration)
        yellow.off()
        
        # Red phase. Red is 5 seconds.
        phase = "red"
        red.on()
        buzzer.beep(on_time = short_beep, off_time = short_beep, background = True)
        sleep(red_light_duration)
        crossing_requested = False
finally:
    # Clean up. This only works with keyboard interrupt.
    red.off()
    yellow.off()
    green.off()
    buzzer.off()
