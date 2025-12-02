# import Pin to use the GPIO pins
from machine import Pin

# import time for sleep function
import time

# set the pins for the LEDs as output
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# set a counter to start at 1
counter = 1

# loop 10 times
while counter < 11:
    print(counter)
    
    # Red ON
    red.value(1)
    amber.value(0)
    green.value(0)

    # wait half a second
    time.sleep(0.5)

    # Amber ON
    red.value(0)
    amber.value(1)
    green.value(0)

    # wait half a second
    time.sleep(0.5)

    # Green ON
    red.value(0)
    amber.value(0)
    green.value(1)

    # wait half a second
    time.sleep(0.5)

    counter += 1

# LEDs OFF
red.value(0)
amber.value(0)
green.value(0)