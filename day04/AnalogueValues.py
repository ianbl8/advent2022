# import ADC and Pin to use the GPIO pins
from machine import ADC, Pin

# import time for sleep function
import time

# set up potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# loop forever
while True:
     
    # potentiometer value
    print(potentiometer.read_u16())
    
    # wait one second
    time.sleep(1)