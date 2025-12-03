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
    if button1.value() == 1 and button2.value() == 1:
        print("Buttons 1 and 2 pressed")
        # turn on green LED and turn off red LED
        green.value(1)
        red.value(0)
        
    # if button1 is pressed, but not button2
    elif button1.value() == 1:
        print("Button 1 pressed")
        # turn on amber LED and turn off red LED
        amber.value(1)
        red.value(0)
        
    # if button1 is not pressed
    else:
        # turn on red LED and turn off green and amber LEDs
        red.value(1)
        amber.value(0)
        green.value(0)