from machine import Pin, ADC

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)

def light_value():
  return sensor.read() * 100 / 4095

def light_is_needed():
  return light_value() > 5