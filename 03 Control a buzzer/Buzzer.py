from gpiozero import Buzzer
from time import sleep

# Buzzer connected to GPIO 15 pin.
buzzer = Buzzer(15)

# Buzz the buzzer in 1 second interval.
while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
