from machine import Pin, PWM
from utime import sleep_ms

servo = PWM(Pin(18), freq=50)

while True:
    for angulo in range(25, 125):
        servo.duty(angulo)
        sleep_ms(50)