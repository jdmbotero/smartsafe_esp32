from machine import Pin, PWM
from utime import sleep_ms

servo = PWM(Pin(15), freq=50)

def open_door():
    servo.duty(30)
    '''i = 72
    while i > 30:
        i = i - 1
        servo.duty(i)
        sleep_ms(50)'''

def close_door():
    servo.duty(72)
    '''i = 30
    while i < 72:
        i = i + 1
        servo.duty(i)
        sleep_ms(50)'''
        
if __name__==("__main__"):
    close_door()