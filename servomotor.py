from machine import Pin, PWM

servo = PWM(Pin(16), freq=50)

def open_door():
    servo.duty(20)

def close_door():
    servo.duty(50)
    
if __name__==("__main__"):
    close_door()