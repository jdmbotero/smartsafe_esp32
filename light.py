from machine import Pin

led = Pin(5, Pin.OUT)

def light_on():
  led.on()

def light_off():
  led.off()