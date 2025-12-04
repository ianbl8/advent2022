# import ADC and Pin to use the GPIO pins
from machine import ADC, Pin

# import time for sleep function
import time

# set up potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# set the pin for the green LED as output
green = Pin(20, Pin.OUT)

# create mydelay variable, start at 0
mydelay = 0

# loop forever
while True:
     
    # update mydelay based on potentiometer value
    mydelay = potentiometer.read_u16() / 65000
    
    # turn on green LED for variable delay period
    green.value(1)
    time.sleep(mydelay)

    # turn off green LED for variable delay period
    green.value(0)
    time.sleep(mydelay)