from utime import sleep
from connection import do_connect, currenttime, gm_time
from firestore import firestore_init, add_or_update_box, get_box_info, add_history_box
from oled import oled_clean, oled_update, show_time, show_distance, show_light_status, show_door_status, show_connection_status
from ultrasonic import distance_cm
from led_rgb import rgb_on_red, rgb_on_turquesa
from light import light_on, light_off
from light_sensor import light_is_needed
from servomotor import open_door, close_door
from magnetic import door_is_open

import _thread

close_door()
do_connect()
firestore_init()

door_status = "CLOSED"
distance = 0.0
light_status = "OFF"
add_or_update_box({"doorStatus": door_status, "distanceObject": distance, "lightStatus": light_status})


def mainLoop():
    global door_status
    global distance
    global light_status
    
    while True:
        # Data from database
        try:
            box_info = get_box_info()
        except:
            box_info = {"doorAction": "CLOSE", "doorStatus": "CLOSE", "connectionStatus": "DISCONNECTED"}
            print("Error occurred in get box info")
        if box_info["doorAction"] == "OPEN":
            if box_info["doorStatus"] == "CLOSED":
                try:
                    add_history_box({"date": gm_time(), "doorAction": "OPEN"})
                except:
                    print("Error occurred in history update")
                open_door()
        else:
            if box_info["doorStatus"] == "OPEN":
                try:
                    add_history_box({"date": gm_time(), "doorAction": "CLOSE"})
                except:
                    print("Error occurred in history update")
                close_door()

        sleep(1)
        if box_info["connectionStatus"] == "CONNECTED":
            rgb_on_turquesa()
            show_connection_status("Conectado")
        else:
            rgb_on_red()
            show_connection_status("Desconectado")

        # Data to update in database
        try:
            add_or_update_box({"doorStatus": door_status, "distanceObject": distance, "lightStatus": light_status})
        except:
            print("Error occurred in box update")
        sleep(1)
    
def timeLoop():
    while True:
        show_time(currenttime())
        sleep(1)
    
def sensorsLoop():
    global door_status
    global distance
    global light_status
    
    while True:
        distance = distance_cm()
        show_distance(distance)
        if light_is_needed():
            light_status = "ON"
            light_on()
            show_light_status("Encendida")
        else:
            light_status = "OFF"
            light_off()
            show_light_status("Apagada")

        if door_is_open() == 1:
            show_door_status("Abierta")
            door_status = "OPEN"
        else:
            show_door_status("Cerrada")
            door_status = "CLOSED"
            
        sleep(0.6)

_thread.start_new_thread(timeLoop, ())
_thread.start_new_thread(sensorsLoop, ())
mainLoop()