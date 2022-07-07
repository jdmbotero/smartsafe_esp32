from machine import Pin, I2C
from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin = 12, echo_pin = 14)

def distance_cm():
    return sensor.distance_cm()