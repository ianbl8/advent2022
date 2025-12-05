# import Pin to use the GPIO pins
from machine import Pin, PWM

# import time for sleep function
import time

# set the pin for the buzzer as PWM
buzzer = PWM(Pin(13))

# set the PWM duty (volume) to 500
buzzer.duty_u16(500)

# set the PWM frequency (tone) to 1000 for a second
buzzer.freq(1000)
time.sleep (1)

# set the PWM frequency (tone) to 500 for a second
buzzer.freq(500)
time.sleep (1)

# mute the buzzer
buzzer.duty_u16(0)