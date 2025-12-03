# import Pin to use the GPIO pins
from machine import Pin

# import time for sleep function
import time

# set up button and its GPIO pin number
# as an input and use a pull down
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)

# loop forever
while True:
    
    # short delay
    time.sleep(0.2)
    
    # if the button is pressed
    if button1.value() == 1:
        print("Button 1 pressed")