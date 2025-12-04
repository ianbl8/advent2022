# import ADC and Pin to use the GPIO pins
from machine import ADC, Pin

# import time for sleep function
import time

# set up potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# set the pins for the LEDs as output
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# create reading variable, start at 0
reading = 0

# loop forever
while True:
     
    # update reading based on potentiometer value
    reading = potentiometer.read_u16()
    print(reading)
    
    # short delay
    time.sleep(0.1)
    
    # light LED based on reading
    if reading <= 21845:
        # red LED on
        red.value(1)
        amber.value(0)
        green.value(0)

    elif 21845 < reading < 43690:
        # amber LED on
        red.value(0)
        amber.value(1)
        green.value(0)

    elif reading >= 43690:
        # green LED on
        red.value(0)
        amber.value(0)
        green.value(1)