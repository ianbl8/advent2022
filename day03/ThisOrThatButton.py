# import Pin to use the GPIO pins
from machine import Pin

# import time for sleep function
import time

# set up buttons and their GPIO pin numbers
# as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# set the pins for the LEDs as output
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# loop forever
while True:
    
    # short delay
    time.sleep(0.2)
    
    # if button1 and button2 are pressed
    if button1.value() == 1 or button2.value() == 1:
        print("Buttons 1 and 2 pressed")
        # turn on green LED
        green.value(1)
        time.sleep(2)
        green.value(0)