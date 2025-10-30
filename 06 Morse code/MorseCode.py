from gpiozero import LED
from gpiozero import Buzzer
from time import sleep

# This program reads user's input, then outputs the corresponding Morse code with a buzzer and an LED.

# Gets references of the buzzer and LED.
buzzer = Buzzer(20)
led = LED(25)

# A unit of time interval used to calculate different intervals used by the Morse code.
unit = 0.5

# A dictionary containing the Morse conversion table for letters and some symbols.
morse_code_dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.',
                    '-':'-....-', '(':'-.--.', ')':'-.--.-'}

# Outputs a dot (.).
def dot():
    led.on()
    buzzer.on()
    sleep(unit)
    led.off()
    buzzer.off()

# Outputs a dash (-).  
def dash():
    led.on()
    buzzer.on()
    sleep(unit * 3)
    led.off()
    buzzer.off()

# Reads a message and convert all letters to uppercase.
message = input("Send a message in Morse code: ").upper()

# Outputs the message one character by one character.
for char in message:
    if char == ' ':
        # 7 units between words.
        sleep(unit * 7)
        continue
    code = morse_code_dict.get(char, '')
    for i, symbol in enumerate(code):
        if symbol == '.':
            dot()
        elif symbol == '-':
            dash()
        # 1 unit between each dot/dash within a character's code.
        if i < len(code) - 1:
            sleep(unit)
    # 3 units between character codes.
    sleep(unit * 3)
