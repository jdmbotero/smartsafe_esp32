from machine import Pin
from utime import sleep_ms

magnetic = Pin(13, Pin.IN)

def door_is_open():
    print(magnetic.value())
    return magnetic.value() == 1

if __name__==("__main__"):
    while True:
        door_is_open()
        sleep_ms(200)