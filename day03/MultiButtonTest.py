# import Pin to use the GPIO pins
from machine import Pin

# import time for sleep function
import time

# set up buttons and their GPIO pin numbers
# as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# loop forever
while True:
    
    # short delay
    time.sleep(0.2)
    
    # if button1 is pressed
    if button1.value() == 1:
        print("Button 1 pressed")
        
    # if button2 is pressed
    if button2.value() == 1:
        print("Button 2 pressed")
        
    # if button3 is pressed
    if button3.value() == 1:
        print("Button 3 pressed")