from machine import Pin
from utime import sleep_ms

magnetic = Pin(17, Pin.IN)

def door_is_open():
    return magnetic.value()

if __name__==("__main__"):
    while True:
        print(door_is_open())
        sleep_ms(200)