# import Pin to use the GPIO pins
from machine import Pin

# import time for sleep function
import time

# set the pins for the LEDs as output
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# turn on the LEDs
red.value(1)
amber.value(1)
green.value(1)
print("LEDs on")

# wait 5 seconds
time.sleep(5)

# turn off the LEDs
red.value(0)
amber.value(0)
green.value(0)
print("LEDs off")