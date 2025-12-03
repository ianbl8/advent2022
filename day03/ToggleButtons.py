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
    time.sleep(0.5)
    
    # if button1 is pressed
    if button1.value() == 1:
        print("Button 1 pressed")
        
        # toggle the red LED on or off
        red.toggle()

    # if button2 is pressed
    elif button2.value() == 1:
        print("Button 2 pressed")
        
        # toggle the amber LED on or off
        amber.toggle()

    # if button3 is pressed
    elif button3.value() == 1:
        print("Button 3 pressed")
        
        # toggle the green LED on or off
        green.toggle()