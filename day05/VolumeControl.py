# import ADC, PWM and Pin to use the GPIO pins
from machine import ADC, PWM, Pin

# import time for sleep function
import time

# set the pin for the buzzer as PWM
buzzer = PWM(Pin(13))

# set the pin for the potentiometer as ADC
potentiometer = ADC(Pin(27))

# create reading and volume variables, start at 0
reading = 0
volume = 0

# loop forever
while True:
    
    # short delay
    time.sleep(0.01)
    
    # update reading based on potentiometer value
    reading = potentiometer.read_u16()

    # convert reading to volume
    # limit to 500 max and allow for 0 volume
    volume = int(reading / 130) - 4
    if volume < 0:
        volume = 0
    print(volume)
    
    # set the PWM frequency (tone) to 500
    buzzer.freq(500)

    # set the PWM duty (volume) to volume
    buzzer.duty_u16(volume)