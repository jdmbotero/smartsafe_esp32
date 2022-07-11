from machine import Pin

sensor = Pin(18, Pin.IN, Pin.PULL_UP)

def door_is_open():
  return sensor.value() == 1