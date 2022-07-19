from machine import Pin

sensor = Pin(13, Pin.IN, Pin.PULL_DOWN)

def door_is_open():
    print(sensor.value())
    return sensor.value() == 1

if __name__==("__main__"):
    while True:
        door_is_open()