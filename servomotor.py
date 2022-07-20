from machine import Pin, PWM
from utime import sleep_ms

servo = PWM(Pin(15), freq=50)

def open_door():
    i = 70
    while i > 20:
        i = i - 1
        servo.duty(i)
        sleep_ms(50)

def close_door():
    i = 20
    while i < 70:
        i = i + 1
        servo.duty(i)
        sleep_ms(50)
    
if __name__==("__main__"):
    close_door()