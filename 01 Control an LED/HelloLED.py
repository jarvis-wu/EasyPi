from gpiozero import LED
from time import sleep

# LED connected to GPIO 25 pin. 
led = LED(25)

# Blink the LED in 1 second interval.
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
