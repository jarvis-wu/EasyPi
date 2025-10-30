from gpiozero import LED
from smbus2 import SMBus
from time import sleep

# This program uses a photoresistor to measure ambient light,
# then uses an ADC to read and convert the light level to digital signal,
# and finally compare the value against a threshold
# to turn on the LED when the surrounding environment is too dark.

# The LED.
led = LED(16)

# A system management bus that uses i2c protocol for ADC to talk to RPi.
bus = SMBus(1)

# The memory address to read from / write to the ADC.
# If using SMBus 1, run `i2cdetect -y 1` to find out the correct address.
adc_addr = 0x4b

# A threshold ambient light level.
threshold = 100

# Reads and returns the value of a given channel from ADC.
def read_adc(channel):
    if not 0 <= channel <= 7:
        raise ValueError("Channel must be 0 to 7.")
    cmd = 0x84 | (channel << 4)
    bus.write_byte(adc_addr, cmd)
    return bus.read_byte(adc_addr)

try:
    while True:
        light_level = read_adc(0) # Read from Channel 0.
        print("Light level:", light_level)
        if light_level < threshold:
            led.on()
        else:
            led.off()
        sleep(1)
except KeyboardInterrupt:
    led.off()
    bus.close()
