# import Pin to use the GPIO pins
from machine import Pin

# set the onboard LED (GPIO25) as output 
onboardLED = Pin(25, Pin.OUT)

# turn the onboard LED on
onboardLED.value(1)
print("The LED is now on.")