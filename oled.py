from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep_ms

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)
print("Oled scan: ", i2c.scan())

def oled_clean():
    oled.fill(0)
    
def show_time(time):
    format_time = str("Hora:  {:02}:{:02}:{:02}".format(time[3], time[4], time[5]))
    print(format_time)
    oled.fill_rect(0, 0, 128, 10, 0)
    oled.text(format_time, 0, 0)
    oled.show()
    
def show_distance(distance):
    format_distance = str("Dist:  {:02.2f}cm".format(distance))
    print(format_distance)
    oled.fill_rect(0, 10, 128, 10, 0)
    oled.text(format_distance, 0, 10)
    oled.show()

def show_light_status(status):
    format_status = str("Luz:   {}".format(status))
    print(format_status)
    oled.fill_rect(0, 20, 128, 10, 0)
    oled.text(format_status, 0, 20)
    oled.show()

def show_door_status(status):
    format_status = str("Puerta:  {}".format(status))
    print(format_status)
    oled.fill_rect(0, 30, 128, 10, 0)
    oled.text(format_status, 0, 30)
    oled.show()

def show_connection_status(status):
    format_status = str("Conex:  {}".format(status))
    print(format_status)
    oled.fill_rect(0, 40, 128, 10, 0)
    oled.text(format_status, 0, 40)
    oled.show()

def oled_update():
    oled.show()
    
if __name__==("__main__"):
    while True:
        show_time((0, 0, 0, 0, 0, 0))
        sleep_ms(200)