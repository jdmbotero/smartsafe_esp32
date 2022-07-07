from utime import sleep
from connection import do_connect, currenttime
from oled import oled_clean, show_time, show_distance
from ultrasonic import distance_cm
from led_rgb import rgb_on_purple
import _thread

def main():
    do_connect()
    is_connected = True

    while True:
        sleep(1)
        oled_clean()
        show_time(currenttime())
        show_distance(distance_cm())
        if is_connected:
            rgb_on_purple()
    
_thread.start_new_thread(main, ())