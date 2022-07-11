from machine import Pin, PWM
from utime import sleep_ms

servo = PWM(Pin(13), freq=50)

def open_door():
    servo.duty(125)

def close_door():
    servo.duty(25)