from machine import Pin, I2C
from hcsr04 import HCSR04
from utime import sleep_ms

hcs = HCSR04(trigger_pin = 13, echo_pin = 14)

def distance_cm():
    return hcs.distance_cm()

if __name__==("__main__"):
    while True:
        print(distance_cm())
        sleep_ms(200)