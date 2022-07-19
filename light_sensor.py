from machine import Pin, ADC
from utime import sleep_ms

ldr = ADC(Pin(33))
ldr.atten(ADC.ATTN_11DB)

def light_value():
  return ldr.read() * 100 / 4095

def light_is_needed():
  return ldr.read() <= 0

if __name__==("__main__"):
    while True:
        print(ldr.read())
        sleep_ms(200)