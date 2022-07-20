from machine import Pin

led = Pin(16, Pin.OUT)

def light_on():
    led.on()

def light_off():
    led.off()
  
if __name__==("__main__"):
    while True:
        light_on()