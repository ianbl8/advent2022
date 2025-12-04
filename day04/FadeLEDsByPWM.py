# import ADC, PWM and Pin to use the GPIO pins
from machine import ADC, PWM, Pin

# import time for sleep function
import time

# set up potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# set the pin for the green LED with PWM
green = PWM(Pin(20))

# set PWM frequency
green.freq(1000)

# create reading variable, start at 0
reading = 0

# loop forever
while True:
     
    # update reading based on potentiometer value
    reading = potentiometer.read_u16()
    print(reading)
    
    # set the green LED PWM cycle to reading
    green.duty_u16(reading)
    
    # very short delay
    time.sleep(0.001)