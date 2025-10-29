from gpiozero import Button
from gpiozero import LED
from time import sleep

# Button connected to GPIO 2 pin.
button = Button(2)

# LED connected to GPIO 25 pin.
led = LED(25)

# Wait for button press.
button.wait_for_press()

# Then turn on the LED for 3 seconds.
led.on()
sleep(3)
led.off()
