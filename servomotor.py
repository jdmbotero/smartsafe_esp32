from machine import Pin, PWM

servo = PWM(Pin(16), freq=45)

def open_door():
    servo.duty(20)

def close_door():
    servo.duty(50)
    
close_door()
if __name__==("__main__"):
    open_door()