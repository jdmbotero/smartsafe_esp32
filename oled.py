from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)
print("Oled scan: ", i2c.scan())

def oled_clean():
    oled.fill(0)
    
def show_time(time):
    format_time = str("Hora: {:02}:{:02}:{:02}".format(time[3], time[4], time[5]))
    print(format_time)
    oled.text(format_time, 0, 0)
    oled.show()
    
def show_distance(distance):
    format_distance = str("Dist: {:02.2f}cm".format(distance))
    print(format_distance)
    oled.text(format_distance, 0, 10)
    oled.show()
